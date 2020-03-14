import logging
from typing import List

import serial.tools.list_ports as list_ports
from serial.tools.list_ports_common import ListPortInfo

logger = logging.getLogger(__name__)

# hardware-dygma-raise-ansi/index.js
DYGMA_VENDOR_ID = 0x1209
DYGMA_PRODUCT_ID = 0x2201


def discover_ports() -> List[ListPortInfo]:
    """Return a list of serial ports with a Dygma keyboard attached to it."""
    ports = list(
        filter(
            lambda port: port.pid == DYGMA_PRODUCT_ID and port.vid == DYGMA_VENDOR_ID,
            list_ports.comports(),
        )
    )

    logger.debug(f"Found ports: {[str(p) for p in ports]}")

    return ports
