import logging
import serial
from serial.tools.list_ports_common import ListPortInfo
from typing import List, Union

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
            raise ValueError(f'{len(layers)} found, 10 layers required')

        self._send('settings.defaultLayer', False)
        self._send('keymap.onlyCustom', True)
        # TODO: keymap.map

    def set_colormap(self, layers: List[Layer]):
        if len(layers) != 10:
            raise ValueError(f'{len(layers)} found, 10 layers required')

        # TODO: palette
        # TODO: colormap.map

    ## Internal Methods ##

    def _send(self, cmd: str, args: Union[DygmaArg, List[DygmaArg]]):
        if not isinstance(args, list):
            args = [args]

        payload = ' '.join([cmd] + [str(_from_arg(arg)) for arg in args])
        logger.debug(f'SEND: {payload}')
        self._conn.write(payload.encode('utf-8') + b'\n')

    def _recv(self) -> List[int]:
        data = []
        while True:
            payload = self._conn.read_until().decode().rstrip()
            if payload == '.':
                break
            else:
                data.extend(int(x) for x in payload.split())
        return data

def _from_arg(arg: DygmaArg) -> int:
    if isinstance(arg, bool):
        return 1 if arg else 0

    if isinstance(arg, int):
        return arg

    raise ValueError(f'Not a valid serial arg: {arg}')
