"""A Color."""

from typing import Any, List, NamedTuple, Tuple

from .serialize import Serializable


class Color(NamedTuple):
    """A Color."""

    red: int
    green: int
    blue: int

    @classmethod
    def from_json(cls, value: Any) -> "Color":
        """Parse a Color from a JSON value."""
        if (
            not isinstance(value, list)
            or len(value) != 3
            or not all(isinstance(x, int) for x in value)
        ):
            raise ValueError("Color needs to be defined as a list of RGB values")

        return Color(*value)


ColorName = str
COLOR_BLACK = "black"


class ColorPalette(Serializable):
    """A Color palette."""

    def __init__(self, palette: List[Tuple[ColorName, Color]]):
        """Initialize a ColorPalette."""
        self._palette = palette

    @classmethod
    def from_json(cls, value: Any) -> "ColorPalette":
        """Parse a ColorPalette from a JSON value."""
        if not isinstance(value, dict):
            raise ValueError("ColorPalette needs to be an object")

        palette = []

        for name, rgb in value.items():
            try:
                color = Color.from_json(rgb)
            except ValueError as e:
                raise ValueError(f"[{name}] {e}")

            palette.append((name, color))

        # black is needed for some defaults
        if not any(name == COLOR_BLACK for name, _ in palette):
            palette.append((COLOR_BLACK, Color(0, 0, 0)))

        return cls(palette)

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
