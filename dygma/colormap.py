"""Generate the color map specified by a palette and layer."""

from typing import List, Mapping, Optional

from .color import ColorName, ColorPalette
from .keys import Key
from .serialize import Serializable


class ColorMap(Serializable):
    """A mapping of physical keys to a color."""

    def __init__(self, palette: ColorPalette, color_map: Mapping[Key, ColorName]):
        """Initialize a ColorMap."""
        self._palette = palette
        self._color_map = color_map

    @classmethod
    def from_layer(
        cls,
        palette: ColorPalette,
        layer_map: Mapping[Key, Optional[ColorName]],
        default_color: ColorName,
        missing_color: ColorName,
    ) -> "ColorMap":
        """
        Initialize a ColorMap from a Layer.

        If the `layer_map` contains a Key mapped to None, then return the
        `default_color`. If the `layer_map` does not contain a Key at all,
        return the `missing_color`.
        """
        color_map = {}
        for key in KEY_MAP:
            if key is None:
                continue

            if key in layer_map:
                color = layer_map[key]
                if color is None:
                    color = default_color
            else:
                color = missing_color

            color_map[key] = color

        return cls(palette, color_map)

    @classmethod
    def deserialize(cls, palette: ColorPalette, data: List[int]) -> "ColorMap":
        """Initialize a ColorMap from a list of numbers sent from the Dygma API."""
        return cls(
            palette,
            {
                key: palette.colors[x]
                for key, x in zip(KEY_MAP, data)
                if key is not None
            },
        )

    def serialize(self) -> List[int]:
        """Serialize this ColorMap into a list of numbers to send to the Dygma API."""
        codes = []
        for key in KEY_MAP:
            if key is None:
                codes.append(0)
                continue

            color_name = self._color_map[key]
            try:
                x = self._palette.colors.index(color_name)
            except IndexError:
                raise ValueError(f"Unknown color: {color_name}")

            codes.append(x)

        return codes


# The order of keys in a Dygma color map
# `None` indicates a key that should always be the base color (e.g. neuron)
KEY_MAP = [
    Key.ESC,
    Key.ONE,
    Key.TWO,
    Key.THREE,
    Key.FOUR,
    Key.FIVE,
    Key.SIX,
    Key.TAB,
    Key.Q,
    Key.W,
    Key.E,
    Key.R,
    Key.T,
    Key.CAPS_LOCK,
    Key.A,
    Key.S,
    Key.D,
    Key.F,
    Key.G,
    Key.LSHIFT,
    Key.ALT_BACKSLASH,
    Key.Z,
    Key.X,
    Key.C,
    Key.V,
    Key.B,
    Key.LCTRL,
    Key.LGUI,
    Key.LALT,
    Key.LSPACE3,
    Key.LSPACE,
    Key.LSPACE2,
    Key.LSPACE1,
    Key.BACKSPACE,
    Key.EQUAL,
    Key.MINUS,
    Key.ZERO,
    Key.NINE,
    Key.EIGHT,
    Key.SEVEN,
    Key.ENTER,
    Key.RBRACK,
    Key.LBRACK,
    Key.P,
    Key.O,
    Key.I,
    Key.U,
    Key.Y,
    Key.BACKSLASH,
    Key.QUOTE,
    Key.SEMICOLON,
    Key.L,
    Key.K,
    Key.J,
    Key.H,
    Key.RSHIFT,
    Key.SLASH,
    Key.PERIOD,
    Key.COMMA,
    Key.M,
    Key.N,
    Key.RCTRL,
    Key.RGUI,
    Key.FN,
    Key.RALT,
    Key.RSPACE3,
    Key.RSPACE,
    Key.RSPACE2,
    Key.RSPACE1,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
]
