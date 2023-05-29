"""A module for latitude and longitude points."""


class Point:
    """Class to represent a point on the earth's surface."""

    def __init__(self, name, latitude, longitude):
        """Initialize the position of the point."""
        self.name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination.")
        self.latitude = latitude
        self.longitude = longitude

    def get_lat_long(self):
        """Return the latitude and longitude of the point."""
        return (self.latitude, self.longitude)
