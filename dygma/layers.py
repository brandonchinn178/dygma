# flake8: noqa
# fmt: off

from enum import Enum

from .utils import *

# TODO: do in configuration file?

COLOR_BLUE = 'BLUE'
COLOR_YELLOW = 'YELLOW'
COLOR_GREEN = 'GREEN'
COLOR_RED = 'RED'
COLOR_ORANGE = 'ORANGE'
COLOR_BLACK = 'BLACK'

PALETTE = [
    ('BLUE', ColorRGB(74, 144, 226)),
    ('YELLOW', ColorRGB(248, 231, 28)),
    ('GREEN', ColorRGB(65, 117, 5)),
    ('RED', ColorRGB(208, 2, 27)),
    ('ORANGE', ColorRGB(245, 166, 35)),
    ('BLACK', ColorRGB(0, 0, 0)),
]

LAYER_0 = Layer(
    base_color=COLOR_BLUE,
    key_map={
        Key.ESC: LayerKey(LayerBaseKey.BACKTICK),
        Key.ONE: LayerKey(LayerBaseKey.ONE),
        Key.TWO: LayerKey(LayerBaseKey.TWO),
        Key.THREE: LayerKey(LayerBaseKey.THREE),
        Key.FOUR: LayerKey(LayerBaseKey.FOUR),
        Key.FIVE: LayerKey(LayerBaseKey.FIVE),
        Key.SIX: LayerKey(LayerBaseKey.SIX),
        Key.SEVEN: LayerKey(LayerBaseKey.SEVEN),
        Key.EIGHT: LayerKey(LayerBaseKey.EIGHT),
        Key.NINE: LayerKey(LayerBaseKey.NINE),
        Key.ZERO: LayerKey(LayerBaseKey.ZERO),
        Key.MINUS: LayerKey(LayerBaseKey.MINUS),
        Key.EQUAL: LayerKey(LayerBaseKey.EQUAL),
        Key.BACKSPACE: LayerKey(LayerBaseKey.BACKSPACE),
        Key.TAB: LayerKey(LayerBaseKey.TAB),
        Key.Q: LayerKey(LayerBaseKey.Q),
        Key.W: LayerKey(LayerBaseKey.W),
        Key.E: LayerKey(LayerBaseKey.E),
        Key.R: LayerKey(LayerBaseKey.R),
        Key.T: LayerKey(LayerBaseKey.T),
        Key.Y: LayerKey(LayerBaseKey.Y),
        Key.U: LayerKey(LayerBaseKey.U),
        Key.I: LayerKey(LayerBaseKey.I),
        Key.O: LayerKey(LayerBaseKey.O),
        Key.P: LayerKey(LayerBaseKey.P),
        Key.LBRACK: LayerKey(LayerBaseKey.LBRACK),
        Key.RBRACK: LayerKey(LayerBaseKey.RBRACK),
        Key.BACKSLASH: LayerKey(LayerBaseKey.BACKSLASH),
        Key.CAPS_LOCK: LayerKey(LayerBaseKey.CAPS_LOCK),
        Key.A: LayerKey(LayerBaseKey.A),
        Key.S: LayerKey(LayerBaseKey.S),
        Key.D: LayerKey(LayerBaseKey.D),
        Key.F: LayerKey(LayerBaseKey.F),
        Key.G: LayerKey(LayerBaseKey.G),
        Key.H: LayerKey(LayerBaseKey.H),
        Key.J: LayerKey(LayerBaseKey.J),
        Key.K: LayerKey(LayerBaseKey.K),
        Key.L: LayerKey(LayerBaseKey.L),
        Key.SEMICOLON: LayerKey(LayerBaseKey.SEMICOLON),
        Key.QUOTE: LayerKey(LayerBaseKey.QUOTE),
        Key.ENTER: LayerKey(LayerBaseKey.ENTER),
        Key.LSHIFT: LayerKey(LayerBaseKey.LSHIFT),
        Key.Z: LayerKey(LayerBaseKey.Z),
        Key.X: LayerKey(LayerBaseKey.X),
        Key.C: LayerKey(LayerBaseKey.C),
        Key.V: LayerKey(LayerBaseKey.V),
        Key.B: LayerKey(LayerBaseKey.B),
        Key.N: LayerKey(LayerBaseKey.N),
        Key.M: LayerKey(LayerBaseKey.M),
        Key.COMMA: LayerKey(LayerBaseKey.COMMA),
        Key.PERIOD: LayerKey(LayerBaseKey.PERIOD),
        Key.SLASH: LayerKey(LayerBaseKey.SLASH),
        Key.RSHIFT: LayerKey(LayerBaseKey.RSHIFT),
        Key.LCTRL: LayerKey(LayerBaseKey.LCTRL),
        Key.LGUI: LayerKey(LayerBaseKey.LGUI),
        Key.LALT: LayerKey(LayerBaseKey.LALT),
        Key.LSPACE_NW: LayerKey(LayerBaseKey.LGUI),
        Key.LSPACE_NE: LayerKey(LayerBaseKey.SPACE),
        Key.LSPACE_SW: LayerKey(LayerBaseKey.SHIFT2, color=COLOR_RED),
        Key.LSPACE_SE: LayerKey(LayerBaseKey.SHIFT1, color=COLOR_YELLOW),
        Key.RSPACE_NW: LayerKey(LayerBaseKey.SPACE),
        Key.RSPACE_NE: LayerKey(LayerBaseKey.RGUI),
        Key.RSPACE_SW: LayerKey(LayerBaseKey.SHIFT1, color=COLOR_YELLOW),
        Key.RSPACE_SE: LayerKey(LayerBaseKey.SHIFT2, color=COLOR_RED),
        Key.RALT: LayerKey(LayerBaseKey.RALT),
        Key.FN: LayerKey(LayerBaseKey.F1),
        Key.RGUI: LayerKey(LayerBaseKey.RGUI),
        Key.RCTRL: LayerKey(LayerBaseKey.RCTRL),
    },
)

LAYER_1 = Layer(
    base_color=COLOR_GREEN,
    key_map={
        Key.TAB: LayerKey(LayerBaseKey.TAB, ctrl=True),

        # spectacle fullscreen/half screens
        Key.W: LayerKey(LayerBaseKey.UP, color=COLOR_ORANGE, alt=True, gui=True),
        Key.S: LayerKey(LayerBaseKey.LEFT, color=COLOR_ORANGE, alt=True, gui=True),
        Key.G: LayerKey(LayerBaseKey.RIGHT, color=COLOR_ORANGE, alt=True, gui=True),
        # spectacle quarter screens
        Key.E: LayerKey(LayerBaseKey.LEFT, color=COLOR_ORANGE, ctrl=True, alt=True),
        Key.R: LayerKey(LayerBaseKey.UP, color=COLOR_ORANGE, ctrl=True, alt=True),
        Key.D: LayerKey(LayerBaseKey.DOWN, color=COLOR_ORANGE, ctrl=True, alt=True),
        Key.F: LayerKey(LayerBaseKey.RIGHT, color=COLOR_ORANGE, ctrl=True, alt=True),

        # arrow keys
        Key.H: LayerKey(LayerBaseKey.LEFT, color=COLOR_GREEN),
        Key.J: LayerKey(LayerBaseKey.DOWN, color=COLOR_GREEN),
        Key.K: LayerKey(LayerBaseKey.UP, color=COLOR_GREEN),
        Key.L: LayerKey(LayerBaseKey.RIGHT, color=COLOR_GREEN),

        Key.LSHIFT: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.LCTRL: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.LALT: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.LSPACE_NW: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.RSHIFT: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.RCTRL: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.RALT: LayerKey(LayerBaseKey.TRANSPARENT),
        Key.RSPACE_NE: LayerKey(LayerBaseKey.TRANSPARENT),
    },
)

LAYER_2 = EMPTY_LAYER

LAYER_3 = EMPTY_LAYER

LAYER_4 = EMPTY_LAYER

LAYER_5 = EMPTY_LAYER

LAYER_6 = EMPTY_LAYER

LAYER_7 = EMPTY_LAYER

LAYER_8 = EMPTY_LAYER

LAYER_9 = EMPTY_LAYER

ALL_LAYERS = [
    LAYER_0,
    LAYER_1,
    LAYER_2,
    LAYER_3,
    LAYER_4,
    LAYER_5,
    LAYER_6,
    LAYER_7,
    LAYER_8,
    LAYER_9,
]
