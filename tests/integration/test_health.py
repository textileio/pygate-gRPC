import logging

from proto.health_rpc_pb2 import STATUS_OK, CheckResponse
from pygate_grpc.health import HealthClient

logger = logging.getLogger(__name__)


def test_grpc_health(pygate_health_client: HealthClient):
    res = pygate_health_client.check()

    assert type(res) == CheckResponse
    assert res.status == STATUS_OK
    assert res.messages == []
