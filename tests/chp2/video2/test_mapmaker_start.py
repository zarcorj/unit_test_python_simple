from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    """Test that a point can be created."""

    p1 = Point("Darkota", 14.234, 16.234)
    assert p1.get_lat_long() == (14.234, 16.234)
