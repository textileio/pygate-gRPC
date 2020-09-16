from pygate_grpc import deals, faults, ffs, health, net, wallet


class PowerGateClient(object):
    def __init__(self, host_name):
        self.health = health.HealthClient(host_name)
        self.faults = faults.FaultsClient(host_name)
        self.deals = deals.DealsClient(host_name)
        self.ffs = ffs.FfsClient(host_name)
        self.wallet = wallet.WalletClient(host_name)
        self.net = net.NetClient(host_name)
