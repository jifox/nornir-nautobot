"""nornir dispatcher for hp_comware devices."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmHPComware(NetmikoDefault):
    """Collection of Napalm Nornir Tasks specific to HPE Comware 5/7 devices."""


class NetmikoHPComware(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to HPE Comware 5/7 devices."""

    config_command = "display current-configuration"
