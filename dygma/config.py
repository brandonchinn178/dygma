"""Definitions for parsing a configuration file."""

from typing import Any, Dict, List, NamedTuple

import yaml

from .api.color import ColorPalette
from .api.keys import Key
from .api.layer import ColoredLayerKey, EMPTY_LAYER, Layer


class Config(NamedTuple):
    """An object containing data parsed from a configuration file."""

    palette: ColorPalette
    layers: List[Layer]

    @classmethod
    def from_json(cls, value: Any) -> "Config":
        """Parse a Config from a JSON value."""
        if not isinstance(value, dict):
            raise ValueError("Configuration needs to be an object")

        raw_palette = value.get("palette")
        if raw_palette is None:
            raise ValueError("Configuration needs a color palette")
        palette = ColorPalette.from_json(raw_palette)

        layers = []
        for i in range(10):
            layer_name = f"layer{i}"
            raw_layer = value.get(layer_name)
            if raw_layer is None:
                layer = EMPTY_LAYER
            elif not isinstance(raw_layer, dict):
                raise ValueError(f"Key '{layer_name}' needs to be an object")
            else:
                layer = parse_layer(raw_layer)

            layers.append(layer)

        return cls(palette, layers)


def read_config(path: str) -> Config:
    """Parse a Config from the given file."""
    raw_config = yaml.load(open(path), Loader=yaml.SafeLoader)
    return Config.from_json(raw_config)


def parse_layer(raw_layer: Dict) -> Layer:
    """Parse a Layer from the given object."""
    base_color = raw_layer.get("base_color")
    if base_color is None:
        raise ValueError("Layer needs a base color")
    if not isinstance(base_color, str):
        raise ValueError("Key 'base_color' needs to be a string")

    layer_map = {}
    raw_keymap = raw_layer.get("keymap", {})
    for raw_key, raw_layer_key in raw_keymap.items():
        key = Key[raw_key]

        try:
            layer_key = ColoredLayerKey.from_json(raw_layer_key)
        except ValueError as e:
            raise ValueError(f"[{raw_key}] {e}")

        layer_map[key] = layer_key

    options = {}
    raw_default_key = raw_layer.get("default_key")
    if raw_default_key is not None:
        try:
            default_key = ColoredLayerKey.from_json(raw_default_key)
        except ValueError as e:
            raise ValueError(f"[default_key] {e}")

        options["default_key"] = default_key

    return Layer(base_color, layer_map, **options)
