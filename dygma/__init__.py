"""An API for communicating with a Dygma keyboard."""

from .api import DygmaConnection
from .discover import discover_ports

__all__ = ["DygmaConnection", "discover_ports"]
