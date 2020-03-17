"""Defines Layer, which contains information to configure a layer."""

from typing import Mapping, NamedTuple, Optional

from .color import COLOR_BLACK, ColorName, ColorPalette
from .colormap import ColorMap
from .keymap import KeyMap
from .keys import Key, LayerBaseKey, LayerKey


class ColoredLayerKey(LayerKey):
    """A LayerKey with a color."""

    def __init__(self, key: LayerBaseKey, color: Optional[ColorName], **kwargs):
        """Initialize a ColoredLayerKey."""
        self._color = color
        super().__init__(key, **kwargs)

    @property
    def color(self) -> Optional[ColorName]:
        """Get the color of the LayerKey."""
        return self._color


class Layer(NamedTuple):
    """Configuration for a layer in the keyboard."""

    # base color of the layer
    # used for underglow, neuron, and LayerKeys without colors defined
    base_color: str

    # missing keys will be set to default_key
    layer_map: Mapping[Key, ColoredLayerKey]

    # default key for missing key map
    default_key: ColoredLayerKey = ColoredLayerKey(LayerBaseKey.DISABLED, COLOR_BLACK)

    def get_keymap(self) -> KeyMap:
        """Get the KeyMap for this layer."""
        return KeyMap.from_layer(self.layer_map, self.default_key)

    def get_colormap(self, palette: ColorPalette) -> ColorMap:
        """Get the ColorMap for this layer."""
        layer_map = {key: layer_key.color for key, layer_key in self.layer_map.items()}
        default_color = self.base_color
        missing_color = self.default_key.color

        if missing_color is None:
            missing_color = COLOR_BLACK

        return ColorMap.from_layer(palette, layer_map, default_color, missing_color)


EMPTY_LAYER = Layer(base_color=COLOR_BLACK, layer_map={})
