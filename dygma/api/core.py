"""Defines DygmaConnection, which can communicate with the Dygma keyboard."""

import logging
from typing import Iterable, List, Union

import serial
from serial.tools.list_ports_common import ListPortInfo

from .color import ColorPalette
from .colormap import ColorMap
from .keymap import KeyMap
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

    def get_keymap(self) -> List[KeyMap]:
        """Get the current keymap configured in the keyboard."""
        data = self._send("keymap.custom")
        keys_per_layer = len(data) // 10

        return [
            KeyMap.deserialize(keymap_data)
            for keymap_data in _chunks(data, keys_per_layer)
        ]

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

    def get_colormap(self, palette: ColorPalette) -> List[ColorMap]:
        """Get the current colormap configured in the keyboard."""
        data = self._send("colormap.map")
        keys_per_layer = len(data) // 10

        return [
            ColorMap.deserialize(palette, colormap_data)
            for colormap_data in _chunks(data, keys_per_layer)
        ]

    def set_colormap(self, palette: ColorPalette, layers: List[Layer]):
        """
        Set the color map to the color map specified in the given layers.

        Requires exactly 10 layers to be provided.
        """
        if len(layers) != 10:
            raise ValueError(f"{len(layers)} found, 10 layers required")

        self._send("palette", palette)

        self._send("colormap.map", [layer.get_colormap(palette) for layer in layers])

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


def _chunks(arr: list, size: int) -> List[list]:
    result = []
    for i in range(0, len(arr), size):
        result.append(arr[i : i + size])  # noqa: E203
    return result
