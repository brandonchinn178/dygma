from .utils import LayerBaseKey, LayerKey


def get_key_code(layer_key: LayerKey) -> int:
    key = layer_key.key
    code = KEY_CODES[key]

    if layer_key.ctrl:
        code += 256

    if layer_key.alt:
        code += 512

    if layer_key.alt_gr:
        code += 1024

    if layer_key.shift:
        code += 2048

    if layer_key.gui:
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
    # ESC
    LayerBaseKey.BACKSPACE: 42,
    # DEL
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
    # ALT_BACKSLASH
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
    # SHIFT0
    LayerBaseKey.SHIFT1: 17451,
    LayerBaseKey.SHIFT2: 17452,
    # SHIFT3
    # SHIFT4
    # SHIFT5
    # SHIFT6
    # SHIFT7
    # SHIFT8
    # SHIFT9
    # SHIFT10
    # LOCK0
    # LOCK1
    # LOCK2
    # LOCK3
    # LOCK4
    # LOCK5
    # LOCK6
    # LOCK7
    # LOCK8
    # LOCK9
    # LOCK10
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
    # LED_NEXT
    # LED_PREV
    # ONE_SHOT0
    # ONE_SHOT1
    # ONE_SHOT2
    # ONE_SHOT3
    # ONE_SHOT4
    # ONE_SHOT5
    # ONE_SHOT6
    # ONE_SHOT7
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
