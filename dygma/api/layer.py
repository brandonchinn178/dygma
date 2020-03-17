"""Defines Layer, which contains information to configure a layer."""

from typing import Any, Mapping, NamedTuple, Optional

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

    @classmethod
    def from_json(cls, value: Any) -> "ColoredLayerKey":
        """Parse a ColoredLayerKey from a JSON value."""
        if isinstance(value, str):
            raw_layer_key = {"key": value}
        elif isinstance(value, dict):
            raw_layer_key = value
        else:
            raise ValueError("Invalid layer key")

        raw_key = raw_layer_key.get("key")
        if raw_key is None:
            raise ValueError(f"Missing layer key")

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

        return cls(layer_base_key, color, **options)

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

    @classmethod
    def from_json(cls, value: Any) -> "Layer":
        """Parse a Layer from the given JSON value."""
        if not isinstance(value, dict):
            raise ValueError(f"Layer needs to be an object")

        base_color = value.get("base_color")
        if base_color is None:
            raise ValueError("Layer needs a base color")
        if not isinstance(base_color, str):
            raise ValueError("Key 'base_color' needs to be a string")

        layer_map = {}
        raw_keymap = value.get("keymap", {})
        for raw_key, raw_layer_key in raw_keymap.items():
            key = Key[raw_key]

            try:
                layer_key = ColoredLayerKey.from_json(raw_layer_key)
            except ValueError as e:
                raise ValueError(f"[{raw_key}] {e}")

            layer_map[key] = layer_key

        options = {}
        raw_default_key = value.get("default_key")
        if raw_default_key is not None:
            try:
                default_key = ColoredLayerKey.from_json(raw_default_key)
            except ValueError as e:
                raise ValueError(f"[default_key] {e}")

            options["default_key"] = default_key

        return cls(base_color, layer_map, **options)

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
