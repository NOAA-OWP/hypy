from typing import Union, Tuple, TYPE_CHECKING
from evaluation_tools import nwis_client

from hypy.hydrolocation import HydroLocation, HydroLocationType

if TYPE_CHECKING:
    from pandas import DataFrame, Timestamp
    from numpy import datetime64
    from datetime import datetime
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

        """
        super().__init__(realized_nexus, shape, HydroLocationType.hydrometricStation, referenced_position)
        self._station_id = station_id
        self._nwis = nwis_client.IVDataService()
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
        return self._nwis.get(self._station_id, startDT=start, endDT=end)
