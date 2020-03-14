#!/usr/bin/env python3

"""Sync keyboard with configuration files."""

import argparse
import logging
from typing import Optional

from dygma import DygmaConnection, discover_ports

from .layers import ALL_LAYERS


def select_port() -> Optional[str]:
    found_ports = discover_ports()

    if len(found_ports) == 0:
        raise Exception("Could not find any connected Dygma keyboards")
    elif len(found_ports) == 1:
        port = found_ports[0]

        print(f"Found device: {port.device}")
        print(f"Use this device? [y/N]")
        if input("> ").lower() != "y":
            print("Exiting...")
            return None
        else:
            return port
    else:
        print("Select device:")
        for i, port in enumerate(found_ports):
            print(f"{i}. {port.device}")

        selected = input("> ")
        return found_ports[selected]


def sync(conn, config_file):
    conn.set_keymap(ALL_LAYERS)
    conn.set_colormap(ALL_LAYERS)


def main():
    parser = argparse.ArgumentParser(description="Run actions using the Dygma API")
    subparsers = parser.add_subparsers()

    upload_parser = subparsers.add_parser(
        "sync", help="Sync layer configuration with the keyboard"
    )
    upload_parser.add_argument(
        "file", metavar="FILE", help="The path to the layer configuration file"
    )
    upload_parser.set_defaults(command="sync")

    args = parser.parse_args()

    port = select_port()
    if port is None:
        return

    conn = DygmaConnection(port)

    if args.command == "sync":
        sync(conn, args.file)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
