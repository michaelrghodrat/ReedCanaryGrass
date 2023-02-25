from __future__ import annotations

class Point:
    """ A point in a 2-dimensional coordinate system, with first coordinate 
    representing degrees longitude, second coordinate representing degrees
    latitude.

    === Attributes ===
    lat: the latitude coordinate
    lon: the longitude coordinate

    === Representation Invariants ===
    Units in this class will always be degrees, e.g. 77 degrees latitude,
    unless otherwise stated.
    """
    lon: float
    lat: float

    def __init__(self, lon: float, lat: float) -> None:
        """ Initialize a point at latitude <lat> and longiude <lon>.

        >>> pt = Point(-77.891, 45.249)
        >>> pt.lat
        45.249
        >>> pt.lon
        -77.891 
        """
        self.lon = lon
        self.lat = lat

    def __str__(self) -> str:
        """ Return a string representation of the point in format (lon, lat).

        >>> pt = Point(-77.891, 45.249)
        >>> print(pt)
        (-77.891, 45.249)
        """
        return f'({self.lon}, {self.lat})'
    
    def _xdisp(self, other: Point) -> float:
        """ Return the displacement in the x, i.e. longitude, direction between
        self and other.

        >>> pt1 = Point(-77.500, 43.200)
        >>> pt2 = Point(-74.500, 44.890)
        >>> pt1._xdisp(pt2)
        3.0
        >>> pt2._xdisp(pt1)
        -3.0
        """
        return other.lon - self.lon

    def _ydisp(self, other: Point) -> float:
        """ Return the displacement in the y, i.e. latitude, direction between
        self and other.

        >>> pt1 = Point(-77.500, 43.200)
        >>> pt2 = Point(93.200, 45.700)
        >>> pt1._ydisp(pt2)
        2.50
        >>> pt2._ydisp(pt1)
        -2.50
        """
        return other.lat - self.lat

    def dist(self, other) -> float:
        """ Return distance, in degrees, between the points <self> and <other>. 

        >>> pt1 = Point(-77.891, 45.249)
        >>> pt2 = Point(-75.891, 47.249)
        >>> pt1.dist(pt2)
        2.828
        """
        return ((self._xdisp(other))**2 + (self._ydisp(other))**2)**(1/2)

    def add(self, other) -> Point:
        """ The result of adding other to self where other is viewed as an
        vector in the tangent space of self. I.e. regular vector addition.

        >>> pt1 = Point(-77.891, 45.249)
        >>> pt2 = Point(0.25, 0.25)
        >>> res = pt1.add(pt2)
        >>> print(res)
        (-77.641, 45.499) 
        """
        return Point(self.lon + other.lon, self.lat + other.lat)





if __name__ == '__main__':
    import doctest
    doctest.testmod()