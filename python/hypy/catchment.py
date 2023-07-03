import pandas as pd
from .formulation import CatchmentFormulation
from .nexus import Nexus
from .realization import Realization
from typing import List, Optional, Tuple, Union

Catchments_Collection = Union['Catchment', List['Catchment'], Tuple['Catchment', ...]]


class Catchment:
    """
    Implementation of the HY Features Catchment concept.

    The type is designed to expect that many of its properties are effectively immutable (though since it's Python, not
    actually) after object initialization.  I.e., most properties should have their values passed in when an object is
    created.  There are a few exceptions explained below, but this should be the default expectation.

    The following properties are designed as potentially mutable after initialization:
        - ::attribute:`formulation`
        - ::attribute:`realization`

    These are implemented with ``@property`` methods so that the getter/setter can be overridden in subtypes if behavior
    needs to be customized.  It is also expected that once these have been set, they may be changed, but they will not
    be unset (i.e., set back to ``None``).

    Further, the following properties are transitive, with ``@property`` getters provided for convenience.  As such,
    they cannot be set directly, and their mutability is subject to the implementation of other types:
        - ::attribute:`lower_catchments` (provided via ::attribute:`outflow)
        - ::attribute:`upper_catchments` (provided via ::attribute:`inflow)
    """

    @classmethod
    def _convert_collection_to_tuple(cls, collection: Catchments_Collection) -> Tuple['Catchment', ...]:
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
        Tuple['Catchment', ...]
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

    #Slots are the attributes of the class (instance variables)
    #A more efficient way of implementing them compared to __dict__
    #Used here since potentially MANY Catchment objects may exist in a single application
    __slots__ = ["_id", "_inflow", "_outflow", "_contained_catchments", "_containing_catchment",
                 "_realization", "_conjoined_catchments"]

    def __init__(self,
                 catchment_id: str,
                 params: dict,
                 inflow: Optional[Nexus] = None,
                 outflow: Optional[Nexus] = None,
                 contained_catchments: Catchments_Collection = tuple(),
                 containing_catchment: Optional['Catchment'] = None,
                 conjoined_catchments: Catchments_Collection = tuple(),
                 realization: Optional[Realization] = None):
        """
        Set the catchment identity and transform the raw params into dataframes.

        Parameters
        ----------
        catchment_id: str
            The identifier string for this catchment.
        params: dict
            Dictionary of params for directly and indirectly configuring the catchment.
        inflow: Nexus
            The inflow/input Nexus for the catchment, or ``None`` if it does not have one.
        outflow: Nexus
            The outflow/output Nexus for the catchment, or ``None`` if it does not have one.
        contained_catchments: Catchments_Collection
            A collection of nested catchments having an "is-in" relationship with this catchment.
        containing_catchment: Optional['Catchment']
            An optional catchment that contains this one.
        conjoined_catchments: Catchments_Collection
            A collection of conjoined catchments related to this catchment.
        realization: Optional[Realization]
            The optional catchment realization object associated with this catchment.
        """
        self._id = catchment_id
        self._inflow = inflow
        self._outflow = outflow
        self._contained_catchments = self._convert_collection_to_tuple(contained_catchments)
        self._containing_catchment = containing_catchment
        self._conjoined_catchments = self._convert_collection_to_tuple(conjoined_catchments)
        self._realization = realization

    @property
    def conjoined_catchments(self) -> Tuple['Catchment', ...]:
        """

        Returns
        -------
        Tuple['Catchment', ...]
            Tuple of catchment objects in a conjoined relationship with this object.
        """
        return self._conjoined_catchments

    @property
    def contained_catchments(self) -> Tuple['Catchment', ...]:
        """
        Tuple of catchment object having an "is-in" relationship with this catchment object.

        Returns
        -------
        Tuple[Catchment, ...]
            Tuple of catchment object having an "is-in" relationship with this catchment object.
        """
        return self._contained_catchments

    @property
    def containing_catchment(self) -> Optional['Catchment']:
        """
        The (optional) catchment with which this catchment has an "is-in" relationship.

        Returns
        -------
        Optional[Catchment]
            The catchment with which this catchment has an "is-in" relationship, or ``None`` if there is not one.
        """
        return self._containing_catchment

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
    def inflow(self) -> Optional[Nexus]:
        """
        In-flowing connected Nexus.

        Returns
        -------
        Optional[Nexus]
            In-flowing connected Nexus.
        """
        return self._inflow

    @property
    def lower_catchments(self) -> Tuple['Catchment', ...]:
        """
        The collection of neighboring catchments immediately below this one in the catchment network.

        This is essentially the collection of receiving catchments of the connected downstream/outflow Nexus.

        Returns
        -------
        Tuple['Catchment', ...]
            The collection of neighboring catchments immediately below this one in the catchment network.
        """
        # TODO: reconcile this with Nexus class once finished.
        return self.outflow.receiving_catchments

    @property
    def outflow(self) -> Optional[Nexus]:
        """
        Out-flowing connected Nexus.

        Returns
        -------
        Optional[Nexus]
            Out-flowing connected Nexus.
        """
        return self._outflow

    @property
    def realization(self) -> Optional[Realization]:
        """
        The optional ::class:`Realization` for this catchment.

        Returns
        -------
        Optional[Realization]
            The ::class:`Realization` for this catchment, or ``None`` if it has not been set.
        """
        return self._realization

    @realization.setter
    def realization(self, realization: Realization):
        self._realization = realization

    @property
    def upper_catchments(self) -> Tuple['Catchment', ...]:
        """
        The collection of neighboring catchments immediately above this one in the catchment network.

        This is essentially the collection of contributing catchments of the connected upstream/inflow Nexus.

        Returns
        -------
        Tuple['Catchment', ...]
            The collection of neighboring catchments immediately above this one in the catchment network.
        """
        # TODO: reconcile this with Nexus class once finished.
        return self.inflow.contributing_catchments


class FormulatableCatchment(Catchment):
    """
    A subtype of ::class:`Catchment` extended to support a ::attribute:`formulation` property for encapsulating model
    formulation logic.

    As with the supertype, this type is designed to expect that many of its properties are effectively immutable (though
    since it's Python, not actually) after object initialization.  However, the ::attribute:`formulation` property is
    an exception to this.  See documentation for ::class:`Catchment` for more thorough explanation of the implications
    of this.
    """

    __slots__ = ["_formulation"]

    def __init__(self,
                 catchment_id: str,
                 params: dict,
                 inflow: Optional[Nexus] = None,
                 outflow: Optional[Nexus] = None,
                 contained_catchments: Catchments_Collection = tuple(),
                 containing_catchment: Optional['Catchment'] = None,
                 conjoined_catchments: Catchments_Collection = tuple(),
                 formulation: Optional[CatchmentFormulation] = None,
                 realization: Optional[Realization] = None):
        """
        Set the catchment identity and transform the raw params into dataframes.

        Parameters
        ----------
        catchment_id: str
            The identifier string for this catchment.
        params: dict
            Dictionary of params for directly and indirectly configuring the catchment.
        inflow: Nexus
            The inflow/input Nexus for the catchment, or ``None`` if it does not have one.
        outflow: Nexus
            The outflow/output Nexus for the catchment, or ``None`` if it does not have one.
        contained_catchments: Catchments_Collection
            A collection of nested catchments having an "is-in" relationship with this catchment.
        containing_catchment: Optional['Catchment']
            An optional catchment that contains this one.
        conjoined_catchments: Catchments_Collection
            A collection of conjoined catchments related to this catchment.
        formulation: Optional[CatchmentFormulation]
            The optional modeling formulation object associated with this catchment.
        realization: Optional[Realization]
            The optional catchment realization object associated with this catchment.
        """
        super().__init__(catchment_id=catchment_id, params=params, inflow=inflow, outflow=outflow,
                         contained_catchments=contained_catchments, containing_catchment=containing_catchment,
                         conjoined_catchments=conjoined_catchments, realization=realization)
        self._formulation = formulation
        if self._formulation is not None:
            self._formulation.catchment = self

    @property
    def formulation(self) -> Optional[CatchmentFormulation]:
        """
        The optional ::class:`CatchmentFormulation` for this catchment.

        Returns
        -------
        Optional[CatchmentFormulation]
            The ::class:`CatchmentFormulation` for this catchment, or ``None`` if it has not been set.
        """
        return self._formulation

    @formulation.setter
    def formulation(self, formulation: CatchmentFormulation):
        self._formulation = formulation



