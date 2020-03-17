"""Defines Layer, which contains information to configure a layer."""

from typing import Mapping, NamedTuple, Optional

from .color import COLOR_BLACK
from .keys import Key, LayerBaseKey


class LayerKey(NamedTuple):
    """Configuration for a specific key in a layer."""

    key: LayerBaseKey
    # defaults to layer's base_color
    color: Optional[str] = None

    # modifiers
    ctrl: bool = False
    shift: bool = False
    alt: bool = False
    alt_gr: bool = False
    gui: bool = False
    modify_when_held: bool = False
    layer_shift_when_held: bool = False


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
