# flake8: noqa

from enum import Enum
from typing import Mapping, NamedTuple, Optional


class ColorRGB(NamedTuple):
    red: int
    green: int
    blue: int


COLOR_BLACK = ColorRGB(0, 0, 0)

# fmt: off

# The physical key on the keyboard
Key = Enum("Key", [
    "ESC", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ZERO", "MINUS", "EQUAL", "BACKSPACE",
    "TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "LBRACK", "RBRACK", "BACKSLASH",
    "CAPS_LOCK", "A", "S", "D", "F", "G", "H", "J", "K", "L", "SEMICOLON", "QUOTE", "ENTER",
    "LSHIFT", "Z", "X", "C", "V", "B", "N", "M", "COMMA", "PERIOD", "SLASH", "RSHIFT",
    "LCTRL", "LGUI", "LALT", "LSPACE_NW", "LSPACE_NE", "LSPACE_SW", "LSPACE_SE", "RSPACE_NW", "RSPACE_NE", "RSPACE_SW", "RSPACE_SE", "RALT", "FN", "RGUI", "RCTRL",
])

# The key mapped in a given layer
LayerBaseKey = Enum("LayerBaseKey", [
    # Letters
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",

    # Digits & Spacing
    "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ZERO",
    "SPACE", "ENTER", "TAB", "ESC", "BACKSPACE", "DEL", "INSERT",

    # FX Keys
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10",
    "F11", "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20",
    "F21", "F22", "F23", "F24",

    # Punctuation & Special Letters
    "MINUS", "EQUAL", "LBRACK", "RBRACK", "BACKSLASH", "SEMICOLON", "QUOTE", "BACKTICK", "COMMA", "PERIOD",
    "SLASH", "CAPS_LOCK", "ALT_BACKSLASH",

    # Navigation & Miscellaneous
    "PAGE_UP", "PAGE_DOWN", "HOME", "END", "LEFT", "DOWN", "UP", "RIGHT", "APP",
    "PRINT_SCREEN", "SCROLL_LOCK", "PAUSE", "CYCLE", "SYSTEM",
    "DISABLED", "TRANSPARENT",

    # Number Pad
    "NUM1", "NUM2", "NUM3", "NUM4", "NUM5", "NUM6", "NUM7", "NUM8", "NUM9", "NUM0",
    "NUM_DOT", "NUM_STAR", "NUM_MINUS", "NUM_PLUS", "NUM_SLASH",

    # Modifiers
    "LCTRL", "LSHIFT", "LALT", "LGUI", "RCTRL", "RSHIFT", "RALT", "RGUI",

    # Shift to Layer
    "SHIFT0", "SHIFT1", "SHIFT2", "SHIFT3", "SHIFT4", "SHIFT5", "SHIFT6", "SHIFT7", "SHIFT8", "SHIFT9",
    "SHIFT10",

    # Lock layer
    "LOCK0", "LOCK1", "LOCK2", "LOCK3", "LOCK4", "LOCK5", "LOCK6", "LOCK7", "LOCK8", "LOCK9",
    "LOCK10",

    # Media
    "MUTE", "TRACK_PLUS", "TRACK_MINUS", "STOP", "PLAY", "VOL_UP", "VOL_DOWN",

    # One shot modifiers
    "ONE_LCTRL", "ONE_LSHIFT", "ONE_LALT", "ONE_LGUI", "ONE_RCTRL", "ONE_RSHIFT", "ONE_RALT", "ONE_RGUI",

    # LED Effects
    "LED_NEXT", "LED_PREV",

    # One shot layers
    "ONE_SHOT0", "ONE_SHOT1", "ONE_SHOT2", "ONE_SHOT3", "ONE_SHOT4", "ONE_SHOT5", "ONE_SHOT6", "ONE_SHOT7",

    # Leader
    "LEAD0", "LEAD1", "LEAD2", "LEAD3", "LEAD4", "LEAD5", "LEAD6", "LEAD7",

    # Space cadet
    "CADET_ENABLE", "CADET_DISABLE",

    # Mouse configuration options
    # Steno
])

LAYER_KEY_CODES = {
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
    # TRANSPARENT

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

# fmt: on


class LayerKey(NamedTuple):
    key: LayerBaseKey
    ctrl: bool = False
    shift: bool = False
    alt: bool = False
    alt_gr: bool = False
    gui: bool = False
    modify_when_held: bool = False
    layer_shift_when_held: bool = False


class Layer(NamedTuple):
    # color of underglow and neuron
    underglow: ColorRGB

    # missing keys will be set to default_key
    key_map: Mapping[Key, LayerKey]

    # missing keys will be set to default_color
    key_colors: Mapping[Key, ColorRGB]

    # default key for missing key map
    default_key: LayerKey = LayerKey(LayerBaseKey.DISABLED)

    # default color for missing key colors
    default_color: ColorRGB = COLOR_BLACK


EMPTY_LAYER = Layer(underglow=COLOR_BLACK, key_map={}, key_colors={})
