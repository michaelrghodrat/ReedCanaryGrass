from __future__ import annotations
from typing import Tuple, TextIO
from point import Point
from observation import Observation
from Cell import Cell
from process_data import *
import pandas as pd
import geopandas as gpd

    

class Grid:
    """ A lightwight abstract representation of a rectangular geographical grid.
    In particular, a dictionary whose key-value pairs are such that a key
    is a cell which comprises the grid and its value is set to 1 if there is an
    observation within the cell, else 0.

    === Public Attributes ===
    bounds: the four points representing the bounds of the grid.
    num_cells: the number of cells in the grid
    cell_size: the size of each cell in the grid.
    occupancy: the percentage of cells in the grid which contain an observation.

    === Private Attributes ===
    _dict: the concrete realization of the grid, i.e. dictionary which contains
           the key, (binary) value pairs.
    """
    bounds: Tuple[Point, Point, Point, Point]
    num_cells: int
    cell_size: float
    occupancy: float
    _dict: dict[Point, int]

    def __init__(self, nw: Point, ne: Point, se: Point, sw: Point, cell_size: float) -> None:
        """ Initialize a Grid covering <nw>, <ne>, <se>, <sw> , with <cell_size>
        and all values initially set to 0.

        >>> nw = Point(-95,55)
        >>> ne = Point(-52,55)
        >>> se = Point(-52, 35)
        >>> sw = Point(-95, 35)
        >>> grid = Grid(nw, ne, se, sw, 0.25)
        """
        #               create grid
        _dict = {}
        self.bounds = []
        # Start at nw coords
        min_lon = nw.lon
        max_lat = nw.lat
        lon_ptr = nw.lon
        lat_ptr = nw.lat
        while lat_ptr > se.lat:
            while lon_ptr < ne.lon:
                _dict[Cell((lon_ptr + cell_size/2, lat_ptr - cell_size/2), cell_size)] = 0
                lon_ptr += cell_size
            lat_ptr -= cell_size
            # Keep track of the max long.
            max_lon = lon_ptr
            lon_ptr = nw.lon
        min_lat = lat_ptr
        #               initialize attributes
        self._dict = _dict
        self.num_cells = len(self._dict)
        self.cell_size = cell_size
        self.bounds = ((min_lon,max_lat), (max_lon, max_lat), (max_lon, min_lat), (min_lon, min_lat))
        self.occupancy = (len([key for key in self._dict if self._dict[key] == 1]) / len(self._dict))


    def __str__(self) -> str:
        """ Return a string representation of the grid.

        >>> nw = Point(-95,55)
        >>> ne = Point(-52,55)
        >>> se = Point(-52, 35)
        >>> sw = Point(-95, 35)
        >>> grid = Grid(nw, ne, se, sw, 0.25)
        >>> print(grid)
        bounds: ((-95, 55), (-52, 55), (-52, 35), (-95, 35)) cells: 13760 occupancy: 0
        """
        return f'{self.bounds} cells: {self.num_cells} occupancy: {self.occupancy}'

    # BRAINSTORM - IDEA
    # Read from file, Create list of Observations
    # from the coords in Observations, find out which cells they correspond to
    # Fill in grid appropriately
    
    def sync(self, df: pd.DataFrame) -> Grid:
        """ Modify the grid so that each cell corresponds to a value of 1 if
        an observation in <file> occurs within the cell, else the cell
        corresponds to a value of 0.

        Precondition: <file> is a csv file that contains all required data to
        create an instance of the <Observation> class
        """
        # Read from file, create list of Observations
        #data = pd.read_csv(file, sep="\t", usecols=['gbifID','scientificName',\
        #     'decimalLatitude', 'decimalLongitude', 'year', 
        #     'basisOfRecord', 'institutionCode']).dropna()
        #data = data[data['year'] < 2022.05] # remove any 2023 records
        data = df[['gbifID', 'scientificName', 'decimalLatitude', 'decimalLongitude', 'year', 'basisOfRecord', 'institutionCode']]

        observations = []
        
        for index, row in data.iterrows():
            observations.append(Observation(row['gbifID'], row['scientificName'], \
                 (row['decimalLongitude'], row['decimalLatitude']), row['year'], row['basisOfRecord'], row['institutionCode']))

        for i in range(len(observations)):
            for cell in self._dict:
                if cell.contains(observations[i]):
                    self._dict[cell] = 1
                    break
        print("done")

        for k, v in self._dict.items():
            print(k,v)

        print("occupied cells: ", len([cell for cell in self._dict if self._dict[cell] == 1]))
        print("total cells: ", len(self._dict))
        self.update_occupancy()

        print(self.occupancy)

    
    def update_occupancy(self) -> None:
        """Modifies self.occupancy with the updated occupancy rate
        """
        self.occupancy = len([key for key in self._dict if self._dict[key] == 1])/ len(self._dict)


    def create_grid_gdf(self) -> geopandas.GeoDataFrame:
        """Create and return a GeoDataFrame object in which each record represents
        a cell in the grid, with columns indicating the earliest observation of 
        Reed Canary Grass, Bulrush, and Giant Bur Reed.

        columns: 
            unique identifier for cell
            bounding box or coordinates
            earliest observation of rcg
            earliest observation of gbr
            earliest observation of br


        """
        grid_dict = self._dict
        for k,v in grid_dict.items():
            
        
        

             



nw = Point(-95,55)
ne = Point(-52,55)
se = Point(-52, 35)
sw = Point(-95, 35)
grid = Grid(nw, ne, se, sw, 0.25)
print(grid.sync(extract_and_clean()))






        
        
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
