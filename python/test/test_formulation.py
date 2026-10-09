import json
import pytest
from pathlib import Path
from typing import Optional, Dict, Type

from hypy import CatchmentFormulation, FormulatableCatchment


# Need subtype that is not abstract
class CatchmentFormulationTestImpl(CatchmentFormulation):

    __slots__ = ['_maxsmc']

    @classmethod
    def factory_create_from_config(cls, local_config: dict, global_config: Optional[dict] = None) -> 'CatchmentFormulationTestImpl':
        # Leave this alone actually
        pass

    @classmethod
    def get_formulation_type(cls) -> str:
        return cls.__name__

    @classmethod
    def get_required_params_for_type(cls) -> Dict[str, Type]:
        return {'maxsmc': float}

    def __init__(self, formulation_id: str, catchment: Optional[FormulatableCatchment], catchment_id: Optional[str] = None):
        super().__init__(formulation_id=formulation_id, catchment=catchment)
        if catchment_id is not None and self.catchment is None:
            self._catchment_id = catchment_id

    @property
    def catchment_id(self) -> str:
        return self.catchment.id if self.catchment is not None else self._catchment_id

    def get_response(self, input_flux: float, **kwargs) -> float:
        return 0.0

    @property
    def required_params(self) -> Dict[str, Type]:
        return self.get_required_params_for_type()


_current_dir = Path(__file__).resolve().parent


@pytest.fixture
def formulation_1():
    """
    """
    id = 'form-test-1'

    data_path = _current_dir.joinpath('data')
    data_file = data_path.joinpath('example_realization_config.json')
    with open(data_file) as fp:
        data = json.load(fp)
    forcing_path = Path(data['catchments']['cat-88']['forcing']['path'])
    forcing_path = data_path.joinpath('forcing').joinpath(forcing_path.name)

    catchment_params = {'forcing': {'path': forcing_path}}

    formulation = CatchmentFormulationTestImpl(id, catchment=None)
    catchment = FormulatableCatchment('cat-test', catchment_params, formulation=formulation)
    yield formulation


@pytest.fixture
def formulation_2():
    """
    """
    id = 'form-test-2'

    data_path = _current_dir.joinpath('data')
    data_file = data_path.joinpath('example_realization_config.json')
    with open(data_file) as fp:
        data = json.load(fp)
    forcing_path = Path(data['catchments']['cat-88']['forcing']['path'])
    forcing_path = data_path.joinpath('forcing').joinpath(forcing_path.name)

    catchment_params = {'forcing': {'path': forcing_path}}

    catchment = FormulatableCatchment('cat-test-2', catchment_params)
    formulation = CatchmentFormulationTestImpl(id, catchment=catchment)
    yield formulation


def test_formulation_1_a(formulation_1):
    """
    Test proper construction of formulation.
    """
    assert formulation_1.id == 'form-test-1'


def test_formulation_1_b(formulation_1):
    """
    Test formulation is associated with catchment
    """
    assert formulation_1.catchment is not None


def test_formulation_1_c(formulation_1):
    """
    Test formulation is associated with catchment that is associated with this catchment.
    """
    assert formulation_1.catchment.formulation.id == 'form-test-1'


def test_formulation_2_a(formulation_2):
    """
    Test proper construction of formulation.
    """
    assert formulation_2.id == 'form-test-2'


def test_formulation_2_b(formulation_2):
    """
    Test formulation is associated with catchment
    """
    assert formulation_2.catchment is not None


def test_formulation_2_c(formulation_2):
    """
    Test formulation is associated with catchment that is associated with this catchment.
    """
    assert formulation_2.catchment.formulation.id == 'form-test-2'
