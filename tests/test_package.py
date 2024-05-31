from __future__ import annotations

import importlib.metadata

import foo_sphere_volume as m


def test_version():
    assert importlib.metadata.version("foo_sphere_volume") == m.__version__
