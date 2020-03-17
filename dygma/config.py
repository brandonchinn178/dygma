"""Definitions for parsing a configuration file."""

from typing import Any, List, NamedTuple

import yaml

from .api.color import ColorPalette
from .api.layer import EMPTY_LAYER, Layer


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
                try:
                    layer = Layer.from_json(raw_layer)
                except ValueError as e:
                    raise ValueError(f"[{layer_name}] {e}")

            layers.append(layer)

        return cls(palette, layers)


def read_config(path: str) -> Config:
    """Parse a Config from the given file."""
    raw_config = yaml.load(open(path), Loader=yaml.SafeLoader)
    return Config.from_json(raw_config)
