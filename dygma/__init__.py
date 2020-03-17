"""An API for communicating with a Dygma keyboard."""

from .api import DygmaConnection
from .config import read_config
from .discover import discover_ports
from .version import __version__

__all__ = ["DygmaConnection", "discover_ports", "read_config", "__version__"]
