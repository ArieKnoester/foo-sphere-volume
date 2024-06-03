# foo-sphere-volume

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

### [TODO List](./TODO.md):

Items I could not complete or were not feasible to complete in the given time
frame.

<!-- SPHINX-START -->

## Description

Calculates the complex (yet fictitious) Foo, et al. parameterization of sphere
volume.

This package was created using the
[scientific-python/cookie](https://github.com/scientific-python/cookie)
template.

## Installation

Install with pip

```
pip install git+https://github.com/ArieKnoester/foo-sphere-volume
```

## Usage: Calculate the volume of a sphere given the radius

```python
from foo_sphere_volume import sphere_volume


# radius is a required keyword argument
print(sphere_volume(radius=1))  # 4.1887902047863905
```

## Compatibility

Only Python 3.8+ is supported.

## How to contribute

If you'd like to contribute to foo-sphere-volume, take a look at
[CONTRIBUTING.md](./.github/CONTRIBUTING.md).

### Contributors

[![Contributors](https://contrib.rocks/image?repo=ArieKnoester/foo-sphere-volume)](https://github.com/ArieKnoester/foo-sphere-volume/graphs/contributors)

## License

MIT

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/ArieKnoester/foo-sphere-volume/workflows/CI/badge.svg
[actions-link]:             https://github.com/ArieKnoester/foo-sphere-volume/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/foo-sphere-volume
[conda-link]:               https://github.com/conda-forge/foo-sphere-volume-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/ArieKnoester/foo-sphere-volume/discussions
[pypi-link]:                https://pypi.org/project/foo-sphere-volume/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/foo-sphere-volume
[pypi-version]:             https://img.shields.io/pypi/v/foo-sphere-volume
[rtd-badge]:                https://readthedocs.org/projects/foo-sphere-volume/badge/?version=latest
[rtd-link]:                 https://foo-sphere-volume.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->
