"""A Color."""

from typing import List, NamedTuple, Tuple


class Color(NamedTuple):
    """A Color."""

    red: int
    green: int
    blue: int


ColorPalette = List[Tuple[str, Color]]

COLOR_BLACK = "black"
