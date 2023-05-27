"""Create a Point class that stores the latitude and longitude of a city."""

class Point():
    def __init__(self, name, latitude, longitude):
        """Initialize the position of the point."""
        if not isinstance(name, str):
            raise TypeError("City name should be a string")
        self.name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination.")
        self.latitude = latitude
        self.longitude = longitude


    def get_lat_long(self):
        """Return the latitude and longitude of the point."""
        return (self.latitude, self.longitude)
