"""Defines Layer, which contains information to configure a layer."""

from typing import Mapping, NamedTuple

from .color import COLOR_BLACK, ColorPalette
from .colormap import ColorMap
from .keymap import KeyMap
from .keys import Key, LayerBaseKey, LayerKey


class Layer(NamedTuple):
    """Configuration for a layer in the keyboard."""

    # base color of the layer
    # used for underglow, neuron, and LayerKeys without colors defined
    base_color: str

    # missing keys will be set to default_key
    layer_map: Mapping[Key, LayerKey]

    # default key for missing key map
    default_key: LayerKey = LayerKey(LayerBaseKey.DISABLED, COLOR_BLACK)

    def get_keymap(self) -> KeyMap:
        """Get the KeyMap for this layer."""
        return KeyMap.from_layer(self.layer_map, self.default_key)

    def get_colormap(self, palette: ColorPalette) -> ColorMap:
        """Get the ColorMap for this layer."""
        return ColorMap.from_layer(
            palette, self.layer_map, self.default_key, self.base_color
        )


EMPTY_LAYER = Layer(base_color=COLOR_BLACK, layer_map={})
