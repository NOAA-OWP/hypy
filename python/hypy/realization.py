from typing import Optional

class Realization(object):
    """
    Implementation of the HY Features Realization concept.

    """

    __slots__ = ['_id', '_catchment_id']

    def __init__(self, 
                 realization_id: str,
                 catchment_id: Optional[str] = None):
        """
        Set the realization identity and parameters

        Parameters
        ----------
        realization_id: str
            The identifier string for this realization
        catchment_id:
            The identifier string for the realized catchment, or ``None`` if it does not have one.
        """
        self._id = realization_id
        self._catchment_id = catchment_id

    @property
    def id(self) -> str:
        """Return realization identifier
        Returns
        -------
            str
                realization identifier
        """
        return self._id

    @property
    def catchment_id(self) -> Optional[str]:
        """Return realization identifier
        Returns
        -------
            str
                The (optional) catchment identifier that the realization points to.
        """
        return self._catchment_id

class Catchment_Area(Realization):
    """
    Subclass of Realization as a catchment area connecting the inflow and outflow of the catchment it realizes

    """
    pass
