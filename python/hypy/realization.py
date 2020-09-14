from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import Series

class Realization(object):
    """

    """
    __slots__ = ['_id', '_forcing']
    def __init__(self, id):
        """

        """
        self._id = id
        pass

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
    def forcing(self) -> 'Series':
        """Return the forcing data for this catchment

            Returns
            -------
                pandas.Series
                    Series of precipitation volume for the catchment indexed by time
        """
        return self._forcing
