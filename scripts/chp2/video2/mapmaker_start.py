"""A module for latitude and longitude points."""

class Point():
    """A class to represent a point on the earth's surface."""

    def __init__(self, name, latitude, longitude):
        """Initialize the position of the point."""
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
    
    def get_lat_long(self):
        """Return the latitude and longitude of the point."""
        return (self._latitude, self._longitude)
