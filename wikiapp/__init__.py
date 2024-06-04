import importlib.metadata
import warnings

try:
    __version__ = importlib.metadata.version("wikiapp_carla")
except importlib.metadata.PackageNotFoundError as e:
    warnings.warn("Could not determine version of wikiapp_carla", stacklevel=1)
    warnings.warn(str(e), stacklevel=1)
    __version__ = "unknown"
