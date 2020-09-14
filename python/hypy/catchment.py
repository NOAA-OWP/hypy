import pandas as pd

class Catchment():
    """
        Catchment data FIXME docstring
    """
    #Slots are the attributes of the class (instance variables)
    #A more efficient way of implementing them compared to __dict__
    #Used here since potentially MANY Catchment objects may exist in a single application
    __slots__ = ["_id", "_forcing", "_formulation", "inflows", "outflows", "recieving_catchments", "contributing_catchments"]

    def __init__(self, id, params):
        """
            Set the catchment identity and transform the raw params into dataframes
        """
        self._id = id
        self._forcing = pd.read_csv(params['forcing']['path'])

    @property
    def id(self) -> str:
        """Return catchment identifier

        Returns
        -------
            str
                catchment identifier
        """
        return self._id

    @property
    def forcing(self) -> pd.Series:
        """Return the forcing data for this catchment

            Returns
            -------
                pandas.Series
                    Series of precipitation volume for the catchment indexed by time
        """
        return self._forcing
