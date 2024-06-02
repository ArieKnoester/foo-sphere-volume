from __future__ import annotations

from foo_sphere_volume.sphere_volume import sphere_volume


def test_sphere_volume():
    expected = 4.1887902047863905
    actual = sphere_volume(radius=1)
    assert expected == actual
