#!/usr/bin/env python3

"""Sync keyboard with configuration files."""

import logging
import serial
import serial.tools.list_ports as list_ports
from typing import List, Optional, Union

from .layers import ALL_LAYERS

logger = logging.getLogger(__name__)

# hardware-dygma-raise-ansi/index.js
DYGMA_VENDOR_ID = 0x1209
DYGMA_PRODUCT_ID = 0x2201

def select_port(): Optional[str]:
    found_ports = list(filter(
        lambda port: port.pid == DYGMA_PRODUCT_ID and port.vid == DYGMA_VENDOR_ID,
        list_ports.comports()
    ))

    if len(found_ports) == 0:
        raise Exception('Could not find any connected Dygma keyboards')
    elif len(found_ports) == 1:
        port = found_ports[0]

        print(f'Found device: {port.device}')
        print(f'Use this device? [y/N]')
        if input('> ').lower() != 'y':
            print('Exiting...')
            return None
        else:
            return port
    else:
        print('Select device:')
        for i, port in enumerate(found_ports):
            print(f'{i}. {port.device}')

        selected = input('> ')
        return found_ports[selected]

SerialArg = Union[int, bool]

class Serial(serial.Serial):
    def _from_arg(self, arg: SerialArg) -> int:
        if isinstance(arg, int):
            return arg
        elif isinstance(arg, bool):
            return 1 if arg else 0
        else:
            raise ValueError(f'Not a valid serial arg: {arg}')

    def send(self, cmd: str, args: Union[SerialArg, List[SerialArg]]):
        if not isinstance(args, list):
            args = [args]

        payload = ' '.join([cmd] + [self._from_arg(arg) for arg in args])
        logger.debug(f'SEND: {payload}')
        self.write(payload.encode('utf-8') + b'\n')

    # def recv(self) -> List[int]:
    #     data = []
    #     while True:
    #         payload = self.read_until().decode().rstrip()
    #         if payload == '.':
    #             break
    #         else:
    #             data.extend(int(x) for x in payload.split())
    #     return data

def main():
    print()

    port = select_port()
    serial = Serial(port.device)
    serial.send('settings.defaultLayer', False)
    serial.send('keymap.onlyCustom', False)
    # TODO: keymap.map
    # TODO: palette
    # TODO: colormap.map

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
