"""
    HY Features Nexus class
"""

class Nexus():
    """

    """
    __slots__ = ['_id']
    def __init__(self, id: str):
        """

        """
        self._id = id

    @property
    def id(self) -> str:
        """

        """
        return self._id
