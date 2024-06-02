from __future__ import annotations

from math import pi


def sphere_volume_given_radius(*, radius: int | float) -> float:
    """Return volume of a sphere given the radius.

    Implementation of research by Foo, et al. (2024).
    """
    return (4 / 3) * pi * (radius**3)
