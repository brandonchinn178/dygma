"""Definitions for parsing a configuration file."""

from typing import Any, Dict, List, NamedTuple, Union

import yaml

from .api.color import ColorPalette
from .api.keys import Key, LayerBaseKey
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

        if not isinstance(raw_layer_key, (str, dict)):
            raise ValueError(f"Invalid value for {raw_key}: {raw_layer_key}")

        layer_map[key] = parse_layer_key(raw_layer_key)

    options = {}
    raw_default_key = raw_layer.get("default_key")
    if raw_default_key is not None:
        if not isinstance(raw_default_key, (str, dict)):
            raise ValueError(f"Invalid value for 'default_key': {raw_default_key}")

        options["default_key"] = parse_layer_key(raw_default_key)

    return Layer(base_color, layer_map, **options)


def parse_layer_key(raw_layer_key: Union[str, Dict]) -> ColoredLayerKey:
    """Parse a LayerKey."""
    if isinstance(raw_layer_key, str):
        raw_layer_key = {"key": raw_layer_key}

    raw_key = raw_layer_key.get("key")
    if raw_key is None:
        raise ValueError(f"Key {raw_key} does not specify a mapped key")

    layer_base_key = LayerBaseKey[raw_key]

    options = {}

    color = raw_layer_key.get("color")

    for option in (
        "ctrl",
        "alt",
        "alt_gr",
        "gui",
        "modify_when_held",
        "layer_shift_when_held",
    ):
        raw_option = raw_layer_key.get(option)
        if raw_option is not None:
            options[option] = raw_option

    return ColoredLayerKey(layer_base_key, color, **options)
