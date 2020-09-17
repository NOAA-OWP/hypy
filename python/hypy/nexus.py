class Nexus():
    """
    Implementation of the HY Features Nexus concept.
    """
    __slots__ = ["_id", "_to_id"]

    def __init__(self, nexus_id: str, to_id: str):
        """
        Set the nexus identity and transform the raw params into dataframes
        
        Parameters
        ----------
        nexus_id: str
            The identifier string for this nexus
        to_id:
            The catchment identifier that is immediately downstream of this nexus
              
        """
        self._id = nexus_id
        self._to_id = to_id
        # TODO: Consider a connected from

    @property
    def id(self) -> str:
        """Return nexus identifier
        Returns
        -------
            str
                nexus identifier
        """
        return self._id

    @property
    def to_id(self) -> str:
        """Return catchment identifier that is immediately downstream of this nexus

        Returns
        -------
            str
                downstream catchment identifier
        """
        return self._to_id

class Observation_Point(Nexus):
    """
    Subclass of Nexus to define a hydrological observation point that could connect to a data source
    from a USGS gaging station as an example.
    """
    pass
