# flake8: noqa

from enum import Enum
from typing import Mapping, NamedTuple, Optional

Color = Enum("Color", ["BLUE", "YELLOW", "GREEN", "RED", "ORANGE", "BLACK"])


class ColorRGB(NamedTuple):
    red: int
    green: int
    blue: int


PALETTE = {
    Color.BLUE: ColorRGB(74, 144, 226),
    Color.YELLOW: ColorRGB(248, 231, 28),
    Color.GREEN: ColorRGB(65, 117, 5),
    Color.RED: ColorRGB(208, 2, 27),
    Color.ORANGE: ColorRGB(245, 166, 35),
    Color.BLACK: ColorRGB(0, 0, 0),
}

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

# fmt: on


class KeyData(NamedTuple):
    key_code: int
    label: str
    extra_label: Optional[str] = None
    verbose: Optional[str] = None


# fmt: off

LAYER_KEY_DATA = {
    LayerBaseKey.A: KeyData(4, "A"),
    LayerBaseKey.B: KeyData(5, "B"),
    LayerBaseKey.C: KeyData(6, "C"),
    LayerBaseKey.D: KeyData(7, "D"),
    LayerBaseKey.E: KeyData(8, "E"),
    LayerBaseKey.F: KeyData(9, "F"),
    LayerBaseKey.G: KeyData(10, "G"),
    LayerBaseKey.H: KeyData(11, "H"),
    LayerBaseKey.I: KeyData(12, "I"),
    LayerBaseKey.J: KeyData(13, "J"),
    LayerBaseKey.K: KeyData(14, "K"),
    LayerBaseKey.L: KeyData(15, "L"),
    LayerBaseKey.M: KeyData(16, "M"),
    LayerBaseKey.N: KeyData(17, "N"),
    LayerBaseKey.O: KeyData(18, "O"),
    LayerBaseKey.P: KeyData(19, "P"),
    LayerBaseKey.Q: KeyData(20, "Q"),
    LayerBaseKey.R: KeyData(21, "R"),
    LayerBaseKey.S: KeyData(22, "S"),
    LayerBaseKey.T: KeyData(23, "T"),
    LayerBaseKey.U: KeyData(24, "U"),
    LayerBaseKey.V: KeyData(25, "V"),
    LayerBaseKey.W: KeyData(26, "W"),
    LayerBaseKey.X: KeyData(27, "X"),
    LayerBaseKey.Y: KeyData(28, "Y"),
    LayerBaseKey.Z: KeyData(29, "Z"),

    LayerBaseKey.ONE: KeyData(30, "1"),
    LayerBaseKey.TWO: KeyData(31, "2"),
    LayerBaseKey.THREE: KeyData(32, "3"),
    LayerBaseKey.FOUR: KeyData(33, "4"),
    LayerBaseKey.FIVE: KeyData(34, "5"),
    LayerBaseKey.SIX: KeyData(35, "6"),
    LayerBaseKey.SEVEN: KeyData(36, "7"),
    LayerBaseKey.EIGHT: KeyData(37, "8"),
    LayerBaseKey.NINE: KeyData(38, "9"),
    LayerBaseKey.ZERO: KeyData(39, "0"),
    LayerBaseKey.SPACE: KeyData(44, "SPACE"),
    LayerBaseKey.ENTER: KeyData(40, "ENTER"),
    LayerBaseKey.TAB: KeyData(43, "TAB"),
    # ESC
    LayerBaseKey.BACKSPACE: KeyData(42, "BACKSPACE", verbose="Backspace"),
    # DEL
    # INSERT

    LayerBaseKey.F1: KeyData(58, "F1"),
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

    LayerBaseKey.MINUS: KeyData(45, "-"),
    LayerBaseKey.EQUAL: KeyData(46, "="),
    LayerBaseKey.LBRACK: KeyData(47, "["),
    LayerBaseKey.RBRACK: KeyData(48, "]"),
    LayerBaseKey.BACKSLASH: KeyData(49, "\\"),
    LayerBaseKey.SEMICOLON: KeyData(51, ";"),
    LayerBaseKey.QUOTE: KeyData(52, "'"),
    LayerBaseKey.BACKTICK: KeyData(53, "`"),
    LayerBaseKey.COMMA: KeyData(54, ","),
    LayerBaseKey.PERIOD: KeyData(55, "."),
    LayerBaseKey.SLASH: KeyData(56, "/"),
    LayerBaseKey.CAPS_LOCK: KeyData(57, "CAPSLOCK", verbose="Caps Lock"),
    # ALT_BACKSLASH

    # PAGE_UP
    # PAGE_DOWN
    # HOME
    # END
    LayerBaseKey.LEFT: KeyData(80, "LEFT"),
    LayerBaseKey.DOWN: KeyData(81, "DOWN"),
    LayerBaseKey.UP: KeyData(82, "UP"),
    LayerBaseKey.RIGHT: KeyData(79, "RIGHT"),
    # APP
    # PRINT_SCREEN
    # SCROLL_LOCK
    # PAUSE
    # CYCLE
    # SYSTEM
    LayerBaseKey.DISABLED: KeyData(0, "XXX", verbose="Disabled"),
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

    LayerBaseKey.LCTRL: KeyData(224, "LEFT CTRL", verbose="Left Control"),
    LayerBaseKey.LSHIFT: KeyData(225, "LEFT SHIFT", verbose="Left Shift"),
    LayerBaseKey.LALT: KeyData(226, "LEFT ALT", verbose="Left Alt"),
    LayerBaseKey.LGUI: KeyData(227, "LEFT GUI", verbose="Left Gui"),
    LayerBaseKey.RCTRL: KeyData(228, "RIGHT CTRL", verbose="Right Control"),
    LayerBaseKey.RSHIFT: KeyData(229, "RIGHT SHIFT", verbose="Right Shift"),
    LayerBaseKey.RALT: KeyData(230, "RIGHT ALT", verbose="AltGr"),
    LayerBaseKey.RGUI: KeyData(231, "RIGHT GUI", verbose="Right Gui"),

    # SHIFT0
    LayerBaseKey.SHIFT1: KeyData(17451, "1", extra_label="SHIFTTO"),
    LayerBaseKey.SHIFT2: KeyData(17452, "2", extra_label="SHIFTTO"),
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
    underglow: Color

    # missing keys will be set to default_key
    key_map: Mapping[Key, LayerKey]

    # missing keys will be set to default_color
    key_colors: Mapping[Key, Color]

    # default key for missing key map
    default_key: LayerKey = LayerKey(LayerBaseKey.DISABLED)

    # default color for missing key colors
    default_color: Color = Color.BLACK


EMPTY_LAYER = Layer(underglow=Color.BLACK, key_map={}, key_colors={})
