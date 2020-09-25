from typing import List, Optional, Tuple, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .catchment import Catchment, Catchments_Collection

class Nexus():
    """
    Implementation of the HY Features Nexus concept.
    """

    @classmethod
    def _convert_collection_to_tuple(cls, collection: 'Catchments_Collection') -> Tuple['Catchment']:
        """
        Convenience method to accept a ``Catchments_Collection``, which is a union of several possible types, and to
        output a tuple of catchments (or an empty tuple).
        Parameters
        ----------
        collection: Catchments_Collection
            A collection of catchment objects, which could be objects within certain containers, an empty container, or
            a single catchment object itself.
        Returns
        -------
        Tuple['Catchment']
            A tuple containing the catchments included directly or in the container parameter object.
        """
        if isinstance(collection, list):
            return tuple(collection)
        elif isinstance(collection, tuple):
            return collection
        # Assuming type hinting is followed, the only thing this should leave is the single catchment
        # TODO: consider whether any cases outside of type hint need to be addressed
        else:
            return (collection,)

    __slots__ = ["_id", "_receiving_catchments", "_contributing_catchments", "_hydro_location"]

    def __init__(self, 
                 nexus_id: str, 
                 hydro_location,
                 receiving_catchments: 'Catchments_Collection' = tuple(),
                 contributing_catchments: 'Catchments_Collection' = tuple()):   
        """
        Set the nexus identity and params
        
        Parameters
        ----------
        nexus_id: str
            The identifier string for this nexus
        receiving_catchments: Catchments_Collection
            The catchment object(s) that receive(s) water from this nexus
        contributing_catchments: Catchments_Collection
            The catchment object(s) that contribute(s) water to this nexus
              
        """
        self._id = nexus_id
        self._hydro_location = hydro_location
        self._receiving_catchments = self._convert_collection_to_tuple(receiving_catchments) 
        self._contributing_catchments = self._convert_collection_to_tuple(contributing_catchments) 

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
    def receiving_catchments (self) -> Tuple['Catchment']:
        """Tuple of Catchment object(s) receiving water from nexus

        Returns
        -------
        Tuple['Catchment']
            Tuple of Catchment object(s) receiving water from nexus 
        """
        return self._receiving_catchments 

    @property
    def contributing_catchments (self) -> Tuple['Catchment']:
        """Tuple of Catchment object(s) contributing water to nexus

        Returns
        -------
        Tuple['Catchment']
            Tuple of Catchment object(s) contributing water to nexus
        """
        return self._contributing_catchments 
