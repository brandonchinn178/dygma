"""A Color."""

from typing import List, NamedTuple, Tuple

from .serialize import Serializable


class Color(NamedTuple):
    """A Color."""

    red: int
    green: int
    blue: int


ColorName = str
COLOR_BLACK = "black"


class ColorPalette(Serializable):
    """A Color palette."""

    def __init__(self, palette: List[Tuple[ColorName, Color]]):
        """Initialize a ColorPalette."""
        self._palette = palette

    def serialize(self) -> List[int]:
        """Serialize this ColorPalette into numbers to send to the Dygma API."""
        data = []
        for _, color in self._palette:
            data += [color.red, color.green, color.blue]
        return data

    @property
    def colors(self) -> List[ColorName]:
        """Get the names of the colors in this palette."""
        return [color for color, _ in self._palette]
