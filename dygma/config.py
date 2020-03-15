"""Definitions for parsing a configuration file."""

from typing import Dict, List, NamedTuple

import yaml

from .color import Color, ColorPalette
from .keys import Key, LayerBaseKey
from .layer import EMPTY_LAYER, Layer, LayerKey


class Config(NamedTuple):
    """An object containing data parsed from a configuration file."""

    palette: ColorPalette
    layers: List[Layer]


def read_config(path: str) -> Config:
    """Parse a Config from the given file."""
    raw_config = yaml.load(open(path))

    if not isinstance(raw_config, dict):
        raise ValueError("Configuration needs to be an object")

    return parse_config(raw_config)


def parse_config(raw_config: Dict) -> Config:
    """Parse a Config from the given object."""
    raw_palette = raw_config.get("palette")
    if raw_palette is None:
        raise ValueError("Configuration needs a color palette")
    if not isinstance(raw_palette, dict):
        raise ValueError("Key 'palette' needs to be an object")

    palette = parse_palette(raw_palette)

    layers = []
    for i in range(10):
        layer_name = f"layer{i}"
        raw_layer = raw_config.get(layer_name)
        if raw_layer is None:
            layer = EMPTY_LAYER
        elif not isinstance(raw_layer, dict):
            raise ValueError(f"Key '{layer_name}' needs to be an object")
        else:
            layer = parse_layer(raw_layer)

        layers.append(layer)

    return Config(palette, layers)


def parse_palette(raw_palette: Dict) -> ColorPalette:
    """Parse a ColorPalette from the given object."""
    palette = []

    for name, rgb in raw_palette.items():
        if (
            not isinstance(rgb, list)
            or len(rgb) != 3
            or not all(isinstance(x, int) for x in rgb)
        ):
            raise ValueError(
                f"Color needs to be defined as a list of RGB values: {name}"
            )

        color = Color(*rgb)
        palette.append((name, color))

    return palette


def parse_layer(raw_layer: Dict) -> Layer:
    """Parse a Layer from the given object."""
    base_color = raw_layer.get("base_color")
    if base_color is None:
        raise ValueError("Layer needs a base color")
    if not isinstance(base_color, str):
        raise ValueError("Key 'base_color' needs to be a string")

    keymap = {}
    raw_keymap = raw_layer.get("keymap", {})
    for raw_key, raw_layer_key in raw_keymap.items():
        key = Key[raw_key]

        if isinstance(raw_layer_key, str):
            raw_layer_key = {"key": raw_layer_key}

        if not isinstance(raw_layer_key, dict):
            raise ValueError(f"Invalid value for {raw_key}: {raw_layer_key}")

        if "key" not in raw_layer_key:
            raise ValueError(f"Key {raw_key} does not specify a mapped key")

        layer_base_key = LayerBaseKey[raw_layer_key.pop("key")]
        keymap[key] = LayerKey(layer_base_key, **raw_layer_key)

    return Layer(base_color, keymap)
