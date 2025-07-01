"""nornir dispatcher for hp_procurve devices."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmHPProcurve(NapalmDefault):
    """Collection of Naplam Nornir Tasks specific to HP Procurve devices."""


class NetmikoHPProcurve(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to HP Procurve devices."""

    config_command = "show running-config"
