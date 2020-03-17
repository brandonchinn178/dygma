"""Defines the Serializable abstract class."""

import abc
from typing import List


class Serializable(abc.ABC):
    """An interface for classes that are serializable to/from the Dygma API."""

    @abc.abstractmethod
    def serialize(self) -> List[int]:
        """Serialize this class into a list of numbers to send to the Dygma API."""
        pass
