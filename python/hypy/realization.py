from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pandas import Series

class Realization(object):
    """

    """
    __slots__ = ['_id']
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
