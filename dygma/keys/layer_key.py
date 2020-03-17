"""Defines Layer, which contains information to configure a layer."""

from typing import NamedTuple, Optional

from .enums import LayerBaseKey


class LayerKey(NamedTuple):
    """Configuration for a specific key in a layer."""

    key: LayerBaseKey
    # defaults to layer's base_color
    color: Optional[str] = None

    # modifiers
    ctrl: bool = False
    shift: bool = False
    alt: bool = False
    alt_gr: bool = False
    gui: bool = False
    modify_when_held: bool = False
    layer_shift_when_held: bool = False

    def to_key_code(self) -> int:
        """Get the key code for this LayerKey."""
        key = self.key
        code = KEY_CODES[key]

        if self.ctrl:
            code += 256

        if self.alt:
            code += 512

        if self.alt_gr:
            code += 1024

        if self.shift:
            code += 2048

        if self.gui:
            code += 4096

        return code


KEY_CODES = {
    LayerBaseKey.A: 4,
    LayerBaseKey.B: 5,
    LayerBaseKey.C: 6,
    LayerBaseKey.D: 7,
    LayerBaseKey.E: 8,
    LayerBaseKey.F: 9,
    LayerBaseKey.G: 10,
    LayerBaseKey.H: 11,
    LayerBaseKey.I: 12,
    LayerBaseKey.J: 13,
    LayerBaseKey.K: 14,
    LayerBaseKey.L: 15,
    LayerBaseKey.M: 16,
    LayerBaseKey.N: 17,
    LayerBaseKey.O: 18,
    LayerBaseKey.P: 19,
    LayerBaseKey.Q: 20,
    LayerBaseKey.R: 21,
    LayerBaseKey.S: 22,
    LayerBaseKey.T: 23,
    LayerBaseKey.U: 24,
    LayerBaseKey.V: 25,
    LayerBaseKey.W: 26,
    LayerBaseKey.X: 27,
    LayerBaseKey.Y: 28,
    LayerBaseKey.Z: 29,
    LayerBaseKey.ONE: 30,
    LayerBaseKey.TWO: 31,
    LayerBaseKey.THREE: 32,
    LayerBaseKey.FOUR: 33,
    LayerBaseKey.FIVE: 34,
    LayerBaseKey.SIX: 35,
    LayerBaseKey.SEVEN: 36,
    LayerBaseKey.EIGHT: 37,
    LayerBaseKey.NINE: 38,
    LayerBaseKey.ZERO: 39,
    LayerBaseKey.SPACE: 44,
    LayerBaseKey.ENTER: 40,
    LayerBaseKey.TAB: 43,
    LayerBaseKey.ESC: 41,
    LayerBaseKey.BACKSPACE: 42,
    LayerBaseKey.DEL: 76,
    # INSERT
    LayerBaseKey.F1: 58,
    # F2
    # F3
    # F4
    # F5
    # F6
    # F7
    # F8
    # F9
    # F10
    # F11
    # F12
    # F13
    # F14
    # F15
    # F16
    # F17
    # F18
    # F19
    # F20
    # F21
    # F22
    # F23
    # F24
    LayerBaseKey.MINUS: 45,
    LayerBaseKey.EQUAL: 46,
    LayerBaseKey.LBRACK: 47,
    LayerBaseKey.RBRACK: 48,
    LayerBaseKey.BACKSLASH: 49,
    LayerBaseKey.SEMICOLON: 51,
    LayerBaseKey.QUOTE: 52,
    LayerBaseKey.BACKTICK: 53,
    LayerBaseKey.COMMA: 54,
    LayerBaseKey.PERIOD: 55,
    LayerBaseKey.SLASH: 56,
    LayerBaseKey.CAPS_LOCK: 57,
    LayerBaseKey.ALT_BACKSLASH: 100,
    # PAGE_UP
    # PAGE_DOWN
    # HOME
    # END
    LayerBaseKey.LEFT: 80,
    LayerBaseKey.DOWN: 81,
    LayerBaseKey.UP: 82,
    LayerBaseKey.RIGHT: 79,
    # APP
    # PRINT_SCREEN
    # SCROLL_LOCK
    # PAUSE
    # CYCLE
    # SYSTEM
    LayerBaseKey.DISABLED: 0,
    LayerBaseKey.TRANSPARENT: 65535,
    # NUM1
    # NUM2
    # NUM3
    # NUM4
    # NUM5
    # NUM6
    # NUM7
    # NUM8
    # NUM9
    # NUM0
    # NUM_DOT
    # NUM_STAR
    # NUM_MINUS
    # NUM_PLUS
    # NUM_SLASH
    LayerBaseKey.LCTRL: 224,
    LayerBaseKey.LSHIFT: 225,
    LayerBaseKey.LALT: 226,
    LayerBaseKey.LGUI: 227,
    LayerBaseKey.RCTRL: 228,
    LayerBaseKey.RSHIFT: 229,
    LayerBaseKey.RALT: 230,
    LayerBaseKey.RGUI: 231,
    LayerBaseKey.SHIFT_TO_0: 17450,
    LayerBaseKey.SHIFT_TO_1: 17451,
    LayerBaseKey.SHIFT_TO_2: 17452,
    LayerBaseKey.SHIFT_TO_3: 17453,
    LayerBaseKey.SHIFT_TO_4: 17454,
    LayerBaseKey.SHIFT_TO_5: 17455,
    LayerBaseKey.SHIFT_TO_6: 17456,
    LayerBaseKey.SHIFT_TO_7: 17457,
    LayerBaseKey.SHIFT_TO_8: 17458,
    LayerBaseKey.SHIFT_TO_9: 17459,
    LayerBaseKey.LOCK_TO_0: 17408,
    LayerBaseKey.LOCK_TO_1: 17409,
    LayerBaseKey.LOCK_TO_2: 17410,
    LayerBaseKey.LOCK_TO_3: 17411,
    LayerBaseKey.LOCK_TO_4: 17412,
    LayerBaseKey.LOCK_TO_5: 17413,
    LayerBaseKey.LOCK_TO_6: 17414,
    LayerBaseKey.LOCK_TO_7: 17415,
    LayerBaseKey.LOCK_TO_8: 17416,
    LayerBaseKey.LOCK_TO_9: 17417,
    # MUTE
    # TRACK_PLUS
    # TRACK_MINUS
    # STOP
    # PLAY
    # VOL_UP
    # VOL_DOWN
    # ONE_LCTRL
    # ONE_LSHIFT
    # ONE_LALT
    # ONE_LGUI
    # ONE_RCTRL
    # ONE_RSHIFT
    # ONE_RALT
    # ONE_RGUI
    LayerBaseKey.LED_NEXT: 17152,
    # LED_PREV
    # ONE_SHOT_0
    # ONE_SHOT_1
    # ONE_SHOT_2
    # ONE_SHOT_3
    # ONE_SHOT_4
    # ONE_SHOT_5
    # ONE_SHOT_6
    # ONE_SHOT_7
    # LEAD0
    # LEAD1
    # LEAD2
    # LEAD3
    # LEAD4
    # LEAD5
    # LEAD6
    # LEAD7
    # CADET_ENABLE
    # CADET_DISABLE
}
