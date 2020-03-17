#!/usr/bin/env python3

"""Run Dygma CLI."""

import argparse
import logging
from typing import Callable, Optional, TypeVar

from .api import DygmaConnection
from .config import read_config
from .discover import discover_ports
from .version import __version__


logging.basicConfig(level=logging.DEBUG)

T = TypeVar("T")


def prompt(cast: Callable[[str], T]) -> T:
    """Prompt the user for input with the given processing function."""
    while True:
        s = input("> ")
        try:
            return cast(s)
        except Exception:
            pass


def select_port(auto_select: bool) -> Optional[str]:
    """Find ports and prompt the user to choose or confirm one."""
    found_ports = discover_ports()

    if len(found_ports) == 0:
        raise Exception("Could not find any connected Dygma keyboards")

    if len(found_ports) == 1:
        port = found_ports[0]

        print(f"Found device: {port.device}")
        print(f"Use this device? [y/N]")

        if not auto_select and prompt(lambda s: s.lower()) != "y":
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


def sync(config_file: str, auto_select: bool):
    """Sync layer configuration with the keyboard."""
    config = read_config(config_file)

    port = select_port(auto_select)
    if port is None:
        return

    conn = DygmaConnection(port)

    conn.set_keymap(config.layers)
    conn.set_colormap(config.palette, config.layers)


def main():
    """Run main function."""
    parser = argparse.ArgumentParser(description="Run actions using the Dygma API")
    parser.add_argument(
        "--version", help="Display the version and exit", action="store_true"
    )

    subparsers = parser.add_subparsers()

    upload_parser = subparsers.add_parser(
        "sync", help="Sync layer configuration with the keyboard"
    )
    upload_parser.add_argument(
        "file", metavar="FILE", help="The path to the layer configuration file"
    )
    upload_parser.add_argument(
        "-y",
        "--yes",
        help="If only one keyboard is found, auto confirm",
        action="store_true",
    )
    upload_parser.set_defaults(command="sync")

    args = parser.parse_args()

    if args.version:
        print(f"Dygma v{__version__}")
        return

    if args.command == "sync":
        sync(args.file, args.yes)
