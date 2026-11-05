"""Visual Compare — classic LiteGraph image inspection for ComfyUI."""

from .visual_compare import VisualCompare

NODE_CLASS_MAPPINGS = {
    "VicVisualCompare": VisualCompare,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VicVisualCompare": "Visual Compare",
}

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
