"""Generate the keymap specified in a Layer."""

from typing import List, Optional

from .keycode import get_key_code
from .keys import Key
from .layer import Layer


def get_keymap(layer: Layer) -> List[int]:
    """Get the keymap specified in the given Layer."""
    return [_get_layer_key_code(layer, key) for key in KEY_MAP]


def _get_layer_key_code(layer: Layer, key: Optional[Key]) -> int:
    if key is None:
        return 0

    layer_key = layer.keymap.get(key, layer.default_key)
    return get_key_code(layer_key)


# The order of keys in a Dygma keymap
# `None` indicates a key that should always be disabled (e.g. underglow lights)
KEY_MAP = [
    Key.ESC,
    Key.ONE,
    Key.TWO,
    Key.THREE,
    Key.FOUR,
    Key.FIVE,
    Key.SIX,
    None,
    None,
    Key.SEVEN,
    Key.EIGHT,
    Key.NINE,
    Key.ZERO,
    Key.MINUS,
    Key.EQUAL,
    Key.BACKSPACE,
    Key.TAB,
    Key.Q,
    Key.W,
    Key.E,
    Key.R,
    Key.T,
    None,
    None,
    Key.Y,
    Key.U,
    Key.I,
    Key.O,
    Key.P,
    Key.LBRACK,
    Key.RBRACK,
    Key.ENTER,
    Key.CAPS_LOCK,
    Key.A,
    Key.S,
    Key.D,
    Key.F,
    Key.G,
    None,
    None,
    None,
    Key.H,
    Key.J,
    Key.K,
    Key.L,
    Key.SEMICOLON,
    Key.QUOTE,
    Key.BACKSLASH,
    Key.LSHIFT,
    None,
    Key.Z,
    Key.X,
    Key.C,
    Key.V,
    Key.B,
    None,
    None,
    None,
    Key.N,
    Key.M,
    Key.COMMA,
    Key.PERIOD,
    Key.SLASH,
    Key.RSHIFT,
    Key.LCTRL,
    Key.LGUI,
    Key.LALT,
    Key.LSPACE_NW,
    Key.LSPACE_NE,
    None,
    Key.LSPACE_SW,
    Key.LSPACE_SE,
    Key.RSPACE_SW,
    Key.RSPACE_SE,
    Key.RSPACE_NW,
    Key.RSPACE_NE,
    Key.RALT,
    Key.FN,
    Key.RGUI,
    Key.RCTRL,
]
