import pandas as pd
from .nexus import Nexus
from .realization import Realization
from typing import List, Optional, Tuple, Union


class Catchment:
    """
    Implementation of the HY Features Catchment concept.
    """
    #Slots are the attributes of the class (instance variables)
    #A more efficient way of implementing them compared to __dict__
    #Used here since potentially MANY Catchment objects may exist in a single application
    __slots__ = ["_id", "_forcing", "_formulation", "_inflow", "_outflow", "_contained_catchments",
                 "_containing_catchment", "_realization"]

    def __init__(self,
                 catchment_id: str,
                 params: dict,
                 inflow: Optional[Nexus] = None,
                 outflow: Optional[Nexus] = None,
                 contained_catchments: Union['Catchment', List['Catchment'], Tuple['Catchment']] = tuple(),
                 containing_catchment: Optional['Catchment'] = None,
                 formulation: Optional[Formulation] = None,
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
        contained_catchments: Union['Catchment', List['Catchment'], Tuple['Catchment']]
            A collection of nested catchments having an "is-in" relationship with this catchment.
        containing_catchment: Optional['Catchment']
            An optional catchment that contains this one.
        realization: Optional[Realization]
            The optional catchment realization object associated with this catchment.
        formulation: Optional[Formulation]
            The optional modeling formulation object associated with this catchment.
        """
        self._id = catchment_id
        self._forcing = pd.read_csv(params['forcing']['path'])
        self._inflow = inflow
        self._outflow = outflow
        if isinstance(contained_catchments, list):
            self._contained_catchments = tuple(contained_catchments)
        elif isinstance(contained_catchments, tuple):
            self._contained_catchments = contained_catchments
        else:
            self._contained_catchments = (contained_catchments,)
        self._containing_catchment = containing_catchment
        self._formulation = formulation
        self._realization = realization
        # TODO: not sure exactly how to implement conjoined_catchment property

    @property
    def contained_catchments(self) -> Tuple['Catchment']:
        """
        Tuple of catchment object having an "is-in" relationship with this catchment object.

        Returns
        -------
        Tuple[Catchment]
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
    def formulation(self) -> Optional[Formulation]:
        """
        The optional ::class:`Formulation` for this catchment.

        Returns
        -------
        Optional[Formulation]
            The ::class:`Formulation` for this catchment, or ``None`` if it has not been set.
        """
        return self._formulation

    @formulation.setter
    def formulation(self, formulation: Formulation):
        self._formulation = formulation

    @property
    def forcing(self) -> pd.Series:
        """Return the forcing data for this catchment

            Returns
            -------
                pandas.Series
                    Series of precipitation volume for the catchment indexed by time
        """
        return self._forcing

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
    def lower_catchments(self) -> Tuple['Catchment']:
        """
        The collection of neighboring catchments immediately below this one in the catchment network.

        This is essentially the collection of receiving catchments of the connected downstream/outflow Nexus.

        Returns
        -------
        Tuple['Catchment']
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
    def upper_catchments(self) -> Tuple['Catchment']:
        """
        The collection of neighboring catchments immediately above this one in the catchment network.

        This is essentially the collection of contributing catchments of the connected upstream/inflow Nexus.

        Returns
        -------
        Tuple['Catchment']
            The collection of neighboring catchments immediately above this one in the catchment network.
        """
        # TODO: reconcile this with Nexus class once finished.
        return self.inflow.contributing_catchments
