"""Defines Layer, which contains information to configure a layer."""

from typing import Mapping, NamedTuple

from .color import COLOR_BLACK
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


EMPTY_LAYER = Layer(base_color=COLOR_BLACK, layer_map={})
