#!/usr/bin/env python3

"""Sync keyboard with configuration files."""

import argparse
import logging
from typing import Callable, Optional, TypeVar

from dygma import DygmaConnection, discover_ports


T = TypeVar("T")


def prompt(cast: Callable[[str], T]) -> T:
    """Prompt the user for input with the given processing function."""
    while True:
        s = input("> ")
        try:
            return cast(s)
        except Exception:
            pass


def select_port() -> Optional[str]:
    """Find ports and prompt the user to choose or confirm one."""
    found_ports = discover_ports()

    if len(found_ports) == 0:
        raise Exception("Could not find any connected Dygma keyboards")
    elif len(found_ports) == 1:
        port = found_ports[0]

        print(f"Found device: {port.device}")
        print(f"Use this device? [y/N]")
        if prompt(lambda s: s.lower()) != "y":
            print("Exiting...")
            return None
        else:
            return port.device
    else:
        print("Select device:")
        for i, port in enumerate(found_ports):
            print(f"{i}. {port.device}")

        selected = prompt(int)
        return found_ports[selected].device


def sync(conn, config_file):
    """Sync layer configuration with the keyboard."""
    # TODO: use config file
    from dygma.layers import ALL_LAYERS, PALETTE

    conn.set_keymap(ALL_LAYERS)
    conn.set_colormap(PALETTE, ALL_LAYERS)


def main():
    """Run main function."""
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
