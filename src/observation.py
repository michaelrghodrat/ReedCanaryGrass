from __future__ import annotations
from point import Point
from typing import Tuple

all_files = ("rcgData.csv", "bulrushData.csv", "gbrData.csv")

class Observation:
    """ A record from GBIF.

    === Attributes ===
    gbifId: Unique GBIF ID number of the observation
    scientific: Scientific name of the species observed
    lon: longitude coordinate of observation
    lat: latitude coordinate of observation
    year: year observation was made
    bor: basis of record of observation
    instCode: GBIF institution code of observing institution
    """
    gbifId: str
    scientific: str
    lon: float
    lat: float
    coords: Point
    year: int
    bor: str
    instCode: str

    def __init__(self, gbifId: str, scientific: str, loc: Tuple[float, float], 
    year: int, bor: str, instCode: str) -> None:
        """ Initialize an observation.

        >>> obs = Observation("100", "Canis Lupis", (-79.901, 43.238), 2006, \
            "HUMAN_OBSERVATION", "124")
        >>> print(obs.lat)
        43.238
        """
        self.gbifId = gbifId
        self.scientific = scientific
        self.lon = loc[0]
        self.lat = loc[1]
        self.coords = Point(self.lon, self.lat)
        self.year = year
        self.bor = bor
        self.instCode = instCode

    def __str__(self) -> str:
        """ Return a string representing the observation.

        >>> obs = Observation("100", "Canis Lupis", (-79.901, 43.238), 2006, "HUMAN_OBSERVATION", "124")
        >>> print(obs)
        ID: 100, Canis Lupis at (-79.901, 43.238), HUMAN_OBSERVATION, inst 124 
        """
        return f'ID: {self.gbifId}, {self.scientific} at {self.coords}, {self.bor}, inst {self.instCode}'

    







if __name__ == '__main__':
    import doctest
    doctest.testmod()
    