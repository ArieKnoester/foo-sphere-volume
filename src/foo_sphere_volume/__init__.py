"""
Copyright (c) 2024 Arie Knoester. All rights reserved.

foo-sphere-volume: Calculate the complex (yet fictitious) Foo, et al. parameterization of sphere volume.
"""

from __future__ import annotations

from ._version import version as __version__
from .sphere_volume import sphere_volume

__all__ = ["__version__", "sphere_volume"]
