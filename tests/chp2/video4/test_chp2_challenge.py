from scripts.chp2.video4.mapmaker_challenge import Point
import pytest


def test_make_one_point():
    """Test that a point can be created."""
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    """Test that invalid points cannot be created."""
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    assert exp.type == ValueError
    assert str(exp.value) == "Invalid latitude, longitude combination."

    with pytest.raises(TypeError) as exp:
        Point(5, 12.11386, 555.08269)
    assert exp.type == TypeError
    assert str(exp.value) == "City name should be a string"
