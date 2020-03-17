"""Defines Layer, which contains information to configure a layer."""

from .enums import LayerBaseKey


class LayerKey:
    """Configuration for a specific key in a layer."""

    def __init__(
        self,
        key: LayerBaseKey,
        *,
        ctrl=False,
        shift=False,
        alt=False,
        alt_gr=False,
        gui=False,
        modify_when_held=False,
        layer_shift_when_held=False,
    ):
        """Initialize a LayerKey."""
        self._key = key
        self._ctrl = ctrl
        self._shift = shift
        self._alt = alt
        self._alt_gr = alt_gr
        self._gui = gui
        self._modify_when_held = modify_when_held
        self._layer_shift_when_held = layer_shift_when_held

    @classmethod
    def from_key_code(cls, code: int) -> "LayerKey":
        """Initialize a LayerKey from the given key code."""
        options = {}
        base_code = code

        # if a key fails this check, it's probably a special key
        if code < 4096 * 2:
            if base_code >= 4096:
                options["gui"] = True
                base_code -= 4096

            if base_code >= 2048:
                options["shift"] = True
                base_code -= 2048

            if base_code >= 1024:
                options["alt_gr"] = True
                base_code -= 1024

            if base_code >= 512:
                options["alt"] = True
                base_code -= 512

            if base_code >= 256:
                options["ctrl"] = True
                base_code -= 256

        try:
            key = KEY_CODES_REV[base_code]
        except KeyError:
            raise ValueError(
                f"Could not deserialize key code: {base_code} (calculated from {code})"
            )

        return cls(key, **options)

    def to_key_code(self) -> int:
        """Get the key code for this LayerKey."""
        key = self._key
        code = KEY_CODES[key]

        if self._ctrl:
            code += 256

        if self._alt:
            code += 512

        if self._alt_gr:
            code += 1024

        if self._shift:
            code += 2048

        if self._gui:
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
    LayerBaseKey.F2: 59,
    LayerBaseKey.F3: 60,
    LayerBaseKey.F4: 61,
    LayerBaseKey.F5: 62,
    LayerBaseKey.F6: 63,
    LayerBaseKey.F7: 64,
    LayerBaseKey.F8: 65,
    LayerBaseKey.F9: 66,
    LayerBaseKey.F10: 67,
    LayerBaseKey.F11: 68,
    LayerBaseKey.F12: 69,
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

KEY_CODES_REV = {code: key for key, code in KEY_CODES.items()}
