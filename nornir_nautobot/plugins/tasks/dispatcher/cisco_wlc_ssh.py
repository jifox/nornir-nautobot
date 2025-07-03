"""nornir dispatcher for cisco_wlc_ssh devices."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmCiscoWlcSsh(NapalmDefault):
    """Collection of Naplam Nornir Tasks specific to Cisco WLC devices."""


class NetmikoCiscoWlcSsh(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to Cisco WLC devices."""

    config_command = "show running-config"
