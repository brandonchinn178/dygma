import logging
from itertools import chain
from typing import Iterable, List, Union

import serial
from serial.tools.list_ports_common import ListPortInfo

from .keymap import get_keymap
from .utils import Layer

logger = logging.getLogger(__name__)

DygmaArg = Union[int, bool]


class DygmaConnection:
    """
    A connection to a Dygma keyboard.

    The primary API when communicating with a Dygma keyboard.
    """

    def __init__(self, port: Union[ListPortInfo, str]):
        device = port.device if isinstance(port, ListPortInfo) else port
        self._conn = serial.Serial(device)

    def set_keymap(self, layers: List[Layer]):
        if len(layers) != 10:
            raise ValueError(f"{len(layers)} found, 10 layers required")

        self._send("settings.defaultLayer", False)
        self._send("keymap.onlyCustom", True)

        data = chain.from_iterable(get_keymap(layer) for layer in layers)

        self._send("keymap.custom", data)

    def set_colormap(self, layers: List[Layer]):
        if len(layers) != 10:
            raise ValueError(f"{len(layers)} found, 10 layers required")

        # TODO: palette
        # TODO: colormap.map

    """Internal Methods"""

    def _send(self, cmd: str, args: Union[DygmaArg, Iterable[DygmaArg]]):
        if not isinstance(args, Iterable):
            args = [args]

        payload = " ".join([cmd] + [str(_from_arg(arg)) for arg in args])
        logger.debug(f"SEND: {payload}")
        self._conn.write(payload.encode("utf-8") + b"\n")

        data = []  # type: List[int]
        while True:
            resp = self._conn.read_until().decode().rstrip()
            logger.debug(f"RECV: {resp}")
            if resp == ".":
                break
            else:
                data.extend(int(x) for x in resp.split())

        return data


def _from_arg(arg: DygmaArg) -> int:
    if isinstance(arg, bool):
        return 1 if arg else 0

    if isinstance(arg, int):
        return arg

    raise ValueError(f"Not a valid serial arg: {arg}")
