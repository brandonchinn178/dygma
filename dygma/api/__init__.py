"""The API for a Dygma keyboard."""

from .color import ColorPalette
from .colormap import ColorMap
from .core import DygmaConnection
from .keymap import KeyMap
from .keys import Key, LayerBaseKey, LayerKey
from .layer import ColoredLayerKey, Layer

__all__ = [
    "ColoredLayerKey",
    "ColorMap",
    "ColorPalette",
    "DygmaConnection",
    "Key",
    "KeyMap",
    "Layer",
    "LayerBaseKey",
    "LayerKey",
]
