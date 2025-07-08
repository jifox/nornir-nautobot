"""nornir dispatcher for cisco ISE."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmCiscoIse(NapalmDefault):
    """Collection of Napalm Nornir Tasks specific to Cisco ISE devices."""


class NetmikoCiscoIse(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to Cisco ISE devices."""

    config_command = "show run"
