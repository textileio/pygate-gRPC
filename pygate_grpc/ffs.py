import grpc

import proto.ffs_rpc_pb2 as ffs_rpc_pb2
import proto.ffs_rpc_pb2_grpc as ffs_rpc_pb2_grpc

TOKEN_KEY = 'x-ffs-token'
CHUNK_SIZE = 1024 * 1024  # 1MB

class FfsClient(object):
    def __init__(self, host_name):
        self.host_name = host_name
        channel = grpc.insecure_channel(host_name)
        self.client = ffs_rpc_pb2_grpc.RPCServiceStub(channel)

    def _getMetaData(self, token):
        return ((TOKEN_KEY, token),)

    def _generateChunks(self, chunks):
        for chunk in chunks:
            yield ffs_rpc_pb2.AddToHotRequest(chunk=chunk)

    def create(self):
        req = ffs_rpc_pb2.CreateRequest()
        return self.client.Create(req)

    def list_api(self):
        req = ffs_rpc_pb2.ListAPIRequest()
        return self.client.ListAPI(req)

    # The metadata is set in here https://github.com/textileio/js-powergate-client/blob/9d1ad04a7e1f2a6e18cc5627751f9cbddaf6fe05/src/util/grpc-helpers.ts#L7
    # Note that you can't have capital letter in meta data field, see here: https://stackoverflow.com/questions/45071567/how-to-send-custom-header-metadata-with-python-grpc
    def addrs_list(self, token):
        req = ffs_rpc_pb2.AddrsRequest()
        return self.client.Addrs(req, metadata=self._getMetaData(token))

    def id_request(self, token):
        req = ffs_rpc_pb2.IDRequest()
        return self.client.ID(req, metadata=self._getMetaData(token))

    # Note that the chunkIter should be an iterator that yield `ffs_rpc_pb2.AddToHotRequest`,
    # it is the caller's responsibility to create the iterator.
    # The provided getFileChunks comes in handy some times.
    def addToHot(self, chunksIter, token):
        return self.client.AddToHot(chunksIter, metadata=self._getMetaData(token))

    def logs(self, cid, token):
        req = ffs_rpc_pb2.WatchLogsRequest(cid=cid)
        return self.client.WatchLogs(req, metadata=self._getMetaData(token))

    def info(self, cid, token):
        req = ffs_rpc_pb2.WatchLogsRequest(cid=cid)
        return self.client.Info(req, metadata=self._getMetaData(token))

    def getFileChunks(self, filename):
        with open(filename, 'rb') as f:
            while True:
                piece = f.read(CHUNK_SIZE)
                if len(piece) == 0:
                    return
                yield ffs_rpc_pb2.AddToHotRequest(chunk=piece)


