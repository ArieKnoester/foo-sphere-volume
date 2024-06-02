from foo_sphere_volume.sphere_volume import sphere_volume_given_radius


def test_sphere_volume_given_radius():
    expected = 4.1887902047863905
    actual = sphere_volume_given_radius(radius=1)
    assert expected == actual
