"""A Color."""

from typing import List, NamedTuple, Tuple


class Color(NamedTuple):
    """A Color."""

    red: int
    green: int
    blue: int


ColorName = str
ColorPalette = List[Tuple[ColorName, Color]]

COLOR_BLACK = "black"
