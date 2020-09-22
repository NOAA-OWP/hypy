from abc import ABC, abstractmethod
from typing import Dict, Optional, Type, TYPE_CHECKING



class Formulation(ABC):
    """

    """
    __slots__ = ['_id']

    @classmethod
    @abstractmethod
    def factory_create_from_config(cls, local_config: dict, global_config: Optional[dict] = None) -> 'Formulation':
        """
        Factory create a new instance from the provide local and (optional) global config.

        Parameters
        ----------
        local_config
        global_config

        Returns
        -------
        Formulation
            A new formulation object.
        """
        pass

    @classmethod
    @abstractmethod
    def get_formulation_type(cls) -> str:
        """
        Get the name of this formulation type that will represent it in serialized configurations to indicate the type
        of formulation to be used.

        Returns
        -------
        str
            The name of this formulation type that will represent it in serialized configurations.
        """
        pass

    @classmethod
    @abstractmethod
    def get_required_params_for_type(cls) -> Dict[str, Type]:
        """
        Get the names of all the required parameters for this formulation type as a dictionary, where the mapped values
        are the acceptable type(s) for each formulation parameter, when these can be universally defined for all
        instances of this particular type (i.e., not subclasses).

        However, all implementations of this type should hold to the invariant that at least one of the following is
        always ``True``:
            - ``self.get_required_params_for_type() == self.required_params()``
            - ``len(self.get_required_params_for_type()) == 0``

        That is, types should ensure the instance and class methods return the equivalent values unless it is not
        possible to define required parameters on the class level, in which case this method should return an empty
        dictionary.

        Returns
        -------
        Dict[str, Type]
            A map of required formulation params to each's expected type(s), applicable to all instances of this type.

        See Also
        -------
        ::method:`required_params`
        """
        pass

    def __init__(self, formulation_id: str):
        self._id = formulation_id

    @property
    def id(self) -> str:
        """
        The formulation identifier.

        Returns
        -------
        str
            The formulation identifier.
        """
        return self._id

    @abstractmethod
    def get_response(self, input_flux: float, **kwargs) -> float:
        pass

    @property
    @abstractmethod
    def required_params(self) -> Dict[str, Type]:
        """
        Get the names of all the required parameters for this formulation as a dictionary, where the mapped values are
        the acceptable type(s) for each formulation parameter.

        However, all implementations of this type should hold to the invariant that at least one of the following is
        always ``True``:
            - ``self.get_required_params_for_type() == self.required_params()``
            - ``len(self.get_required_params_for_type()) == 0``

        Returns
        -------
        Dict[str, Type]
            A map of required formulation parameters to each's expected type(s).

        See Also
        -------
        ::method:`get_required_params_for_type`
        """
        pass
