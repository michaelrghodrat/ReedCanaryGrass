from __future__ import annotations
from typing import Tuple, TextIO
from point import Point
from observation import Observation
import pandas as pd


class Cell:
    """ A geographical square plot of land.

    === Attributes ===
    ctr: the coordinates of the centre of the cell
    size: the size of the cell (in degrees)
    nw: the coordinates of the north-west corner of the cell
    sw: the coordinates of the south-west corner of the cell
    ne: the coordinates of the north-east corner of the cell
    se: the coordinates of the south-east corner of the cell
    """
    ctr: Point
    size: float
    nw: Point
    sw: Point
    ne: Point
    se: Point

    def __init__(self, centre: tuple[float, float], size: float) -> None:
        """ Initialize a cell of <size> with <ctr> coordinates.

        >>> cell = Cell((-78.899, 45.520), 0.5)
        >>> print(cell.se)
        (-78.649, 45.270)
        """
        self.ctr = Point(centre[0], centre[1])
        self.nw = Point(centre[0] - size/2, centre[1] + size/2)
        self.ne = Point(centre[0] + size/2, centre[1] + size/2)
        self.se = Point(centre[0] + size/2, centre[1] - size/2)
        self.sw = Point(centre[0] - size/2, centre[1] - size/2)
        self.size = size
    
    def __str__(self) -> str:
        """ A string representation of a cell.

        >>> cell = Cell((-78.899, 45.520), 0.5)
        >>> print(cell)
        (-79.149, 45.770) (-78.649, 45.770) (-78.649, 45.270) (-79.149, 45.270)
        """
        return f'{self.nw} {self.ne} {self.se} {self.sw}'

    def contains(self, obs: Observation) -> bool:
        """ Return True if an observation <obs> is physically contained
        within the geographical boundaries of cell <self>. Else return False.

        >>> cell = Cell((-78.899, 45.520), 0.5)
        >>> obs1 = Observation("100", "Canis Lupis", (-79.901, 43.238), 2006, \
            "HUMAN_OBSERVATION", "124")
        >>> obs2 = Observation("100", "Canis Lupis", (-79.001, 45.510), 2006, \
            "HUMAN_OBSERVATION", "124")
        >>> cell.contains(obs1)
        False
        >>> cell.contains(obs2)
        True
        """
        return (abs(self.ctr._ydisp(obs.coords)) <= (self.size)/2) and \
            (abs(self.ctr._xdisp(obs.coords)) <= (self.size)/2)
