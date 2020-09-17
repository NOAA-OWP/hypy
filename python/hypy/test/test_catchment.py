import pytest
from typing import Generator
from pathlib import Path
import json

from hypy import Catchment

"""
    Test suite for Catchment class
"""
_current_dir = Path(__file__).resolve().parent


@pytest.fixture
def catchment() -> Generator[Catchment, None, None]:
    """
        Staging of a generator to test
    """
    data_path = _current_dir.joinpath('data')
    data_file = data_path.joinpath('example_realization_config.json')
    with open(data_file) as fp:
        data = json.load(fp)
    forcing_path = Path(data['catchments']['cat-88']['forcing']['path'])
    forcing_path = data_path.joinpath('forcing').joinpath(forcing_path.name)

    params = {'forcing': {'path': forcing_path}}
    yield Catchment('cat-test', params)


@pytest.fixture
def hymod_formulation() -> Generator[Catchment, None, None]:
    """
        Test a mock hymod catchment definition
    """
    catchment_id = 'cat-hymod'
    params = {'sr': [1.0, 1.0, 1.0], 'storage': 1.0, 'max_storage': 1000.0,
              'a': 1.0, 'b': 10.0, 'Ks': 0.1, 'Kq': 0.01, 'n': 3, 't': 0}

    yield Catchment(catchment_id, params)


def test_catchment(catchment: Catchment) -> None:
    """
        Test catchment is properly constructed
    """
    assert catchment.id == 'cat-test'
