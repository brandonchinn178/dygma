# flake8: noqa
# fmt: off

"""Keys on the keyboard."""

from enum import Enum

# The physical key on the keyboard
Key = Enum("Key", [
    # Standard ANSI keyboard
    "ESC", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ZERO", "MINUS", "EQUAL", "BACKSPACE",
    "TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "LBRACK", "RBRACK", "BACKSLASH",
    "CAPS_LOCK", "A", "S", "D", "F", "G", "H", "J", "K", "L", "SEMICOLON", "QUOTE", "ENTER",
    "LSHIFT", "Z", "X", "C", "V", "B", "N", "M", "COMMA", "PERIOD", "SLASH", "RSHIFT",
    "LCTRL", "LGUI", "LALT", "LSPACE_NW", "LSPACE_NE", "LSPACE_SW", "LSPACE_SE", "RSPACE_NW", "RSPACE_NE", "RSPACE_SW", "RSPACE_SE", "RALT", "FN", "RGUI", "RCTRL",

    # Other keys
    "ALT_BACKSLASH",
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
    "SHIFT_TO_0", "SHIFT_TO_1", "SHIFT_TO_2", "SHIFT_TO_3", "SHIFT_TO_4", "SHIFT_TO_5", "SHIFT_TO_6", "SHIFT_TO_7", "SHIFT_TO_8", "SHIFT_TO_9",

    # Lock layer
    "LOCK_TO_0", "LOCK_TO_1", "LOCK_TO_2", "LOCK_TO_3", "LOCK_TO_4", "LOCK_TO_5", "LOCK_TO_6", "LOCK_TO_7", "LOCK_TO_8", "LOCK_TO_9",

    # Media
    "MUTE", "TRACK_PLUS", "TRACK_MINUS", "STOP", "PLAY", "VOL_UP", "VOL_DOWN",

    # One shot modifiers
    "ONE_LCTRL", "ONE_LSHIFT", "ONE_LALT", "ONE_LGUI", "ONE_RCTRL", "ONE_RSHIFT", "ONE_RALT", "ONE_RGUI",

    # LED Effects
    "LED_NEXT", "LED_PREV",

    # One shot layers
    "ONE_SHOT_0", "ONE_SHOT_1", "ONE_SHOT_2", "ONE_SHOT_3", "ONE_SHOT_4", "ONE_SHOT_5", "ONE_SHOT_6", "ONE_SHOT_7",

    # Leader
    "LEAD0", "LEAD1", "LEAD2", "LEAD3", "LEAD4", "LEAD5", "LEAD6", "LEAD7",

    # Space cadet
    "CADET_ENABLE", "CADET_DISABLE",

    # Mouse configuration options
    # Steno
])
