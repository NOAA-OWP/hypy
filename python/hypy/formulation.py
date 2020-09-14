

class Formulation(object):
    """

    """
    __slots__ = ['_id']
    def __init__(self, id):
        """

        """
        self._id = id

    @property
    def id(self) -> str:
        """Return formulation identifier

        Returns
        -------
            str
                formulation identifier
        """
        return self._id
