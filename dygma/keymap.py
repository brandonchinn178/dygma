"""Generate the keymap specified in a Layer."""

from typing import List, Mapping

from .keys import Key, LayerKey
from .serialize import Serializable


class KeyMap(Serializable):
    """A mapping of physical keys to a LayerKey."""

    def __init__(self, key_map: Mapping[Key, LayerKey]):
        """Initialize a KeyMap."""
        self._key_map = key_map

    @classmethod
    def from_layer(
        cls, layer_map: Mapping[Key, LayerKey], default_key: LayerKey
    ) -> "KeyMap":
        """Initialize a KeyMap from a Layer."""
        return cls(
            {key: layer_map.get(key, default_key) for key in KEY_MAP if key is not None}
        )

    @classmethod
    def deserialize(cls, data: List[int]) -> "KeyMap":
        """Initialize a KeyMap from a list of numbers sent from the Dygma API."""
        return cls(
            {
                key: LayerKey.from_key_code(x)
                for key, x in zip(KEY_MAP, data)
                if key is not None
            }
        )

    def serialize(self) -> List[int]:
        """Serialize this KeyMap into a list of numbers to send to the Dygma API."""
        return [
            self._key_map[key].to_key_code() if key is not None else 0
            for key in KEY_MAP
        ]


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
    Key.ALT_BACKSLASH,
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
    Key.LSPACE3,
    Key.LSPACE,
    None,
    Key.LSPACE2,
    Key.LSPACE1,
    Key.RSPACE1,
    Key.RSPACE2,
    Key.RSPACE,
    Key.RSPACE3,
    Key.RALT,
    Key.FN,
    Key.RGUI,
    Key.RCTRL,
]
