"""Defines Layer, which contains information to configure a layer."""

from typing import NamedTuple, Optional

from .enums import LayerBaseKey


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
