from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    """Test that a point can be created."""

    p1 = Point("Darkota", 14.234, 16.234)
    assert p1.get_lat_long() == (14.234, 16.234)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.11386, -555.08269)
    assert exp.type == ValueError
    assert str(exp.value) == "Invalid latitude, longitude combination."
