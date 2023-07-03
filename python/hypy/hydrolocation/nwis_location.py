from typing import Union, Tuple, TYPE_CHECKING
from hydrotools import nwis_client

from hypy.hydrolocation import HydroLocation, HydroLocationType

if TYPE_CHECKING:
    from pandas import DataFrame, Timestamp
    from numpy import datetime64
    from datetime import datetime
    from shapely.geometry import Point
class NWISLocation(HydroLocation):
    """
        An NWIS subclass of HydroLocation
    """
    def __init__(self,
                station_id: str,
                realized_nexus: str,
                shape: Union['Point', Tuple] = None,
                referenced_position = None, #TODO implement indirect position?
                ):
        """

        Parameters
        ----------
        shape: Union[Point, Tuple]
            a shapely point geometry or two-tuple defining the coordinates of this location
        station_id: str
            NWIS station identifier 
        referenced_position:
            position expressed as measured or otherwise described distance from a known, already located referent
        realized_nexus: str
            the nexus identifier associated with this location
        """
        super().__init__(realized_nexus, shape, HydroLocationType.hydrometricStation, referenced_position)
        self._station_id = station_id
        #self._nwis = nwis_client.IVDataService()
    @property
    def station_id(self) -> str:
        """
            NWIS station identifier
        """
        return self._station_id

    def get_data(self,
                 start: Union[ str, 'datetime', 'datetime64', 'Timestamp', None ] = None,
                 end: Union[ str, 'datetime', 'datetime64', 'Timestamp', None ] = None
                 ) -> 'DataFrame':
        """
            Get observation data from nwis
        """
        return nwis_client.IVDataService().get(self._station_id, startDT=start, endDT=end)
