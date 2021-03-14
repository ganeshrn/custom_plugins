def ping(*args, **kwargs):
    ip_addresses = args[0]
    vrf_and_vlan = kwargs.get('vrf_and_vlan')
    commands = []
    for ipaddr in ip_addresses:
        for source_if, vrf in vrf_and_vlan.items():
            commands.append(f"ping {ipaddr} source-interface {source_if} vrf {vrf}")

    return commands


class FilterModule(object):
    """ path filters """

    def filters(self):
        return {"ping": ping}