"""Defines DygmaConnection, which can communicate with the Dygma keyboard."""

import logging
from itertools import chain
from typing import Iterable, List, Union

import serial
from serial.tools.list_ports_common import ListPortInfo

from .color import ColorPalette
from .colormap import get_colormap
from .layer import Layer
from .serialize import Serializable

logger = logging.getLogger(__name__)

DygmaArg = Union[int, bool, Serializable]


class DygmaConnection:
    """
    A connection to a Dygma keyboard.

    The primary API when communicating with a Dygma keyboard.
    """

    def __init__(self, port: Union[ListPortInfo, str]):
        """Initialize a DygmaConnection."""
        device = port.device if isinstance(port, ListPortInfo) else port
        self._conn = serial.Serial(device)

    def __del__(self):
        """Close connection after a DygmaConnection is garbage collected."""
        self.close()

    def close(self):
        """Close connection."""
        if hasattr(self, "_conn"):
            self._conn.close()

    """Dygma API"""

    def set_keymap(self, layers: List[Layer]):
        """
        Set the keymap to the key map specified in the given layers.

        Requires exactly 10 layers to be provided.
        """
        if len(layers) != 10:
            raise ValueError(f"{len(layers)} found, 10 layers required")

        self._send("settings.defaultLayer", False)
        self._send("keymap.onlyCustom", True)

        self._send("keymap.custom", [layer.get_keymap() for layer in layers])

    def set_colormap(self, palette: ColorPalette, layers: List[Layer]):
        """
        Set the color map to the color map specified in the given layers.

        Requires exactly 10 layers to be provided.
        """
        if len(layers) != 10:
            raise ValueError(f"{len(layers)} found, 10 layers required")

        color_palette = chain.from_iterable(
            [color.red, color.green, color.blue] for _, color in palette
        )
        self._send("palette", color_palette)

        all_colors = [color for color, _ in palette]
        colormap = chain.from_iterable(
            get_colormap(all_colors, layer) for layer in layers
        )
        self._send("colormap.map", colormap)

    """Internal Methods"""

    def _send(
        self, cmd: str, args: Union[None, DygmaArg, Iterable[DygmaArg]] = None
    ) -> List[int]:
        """
        Send the given command and arguments to the Dygma keyboard.

        Returns data sent back by the keyboard.
        """
        if args is None:
            args = []
        elif not isinstance(args, Iterable):
            args = [args]

        payload = " ".join([cmd] + [str(x) for arg in args for x in _from_arg(arg)])
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


def _from_arg(arg: DygmaArg) -> List[int]:
    if isinstance(arg, bool):
        return [1] if arg else [0]

    if isinstance(arg, int):
        return [arg]

    return arg.serialize()
