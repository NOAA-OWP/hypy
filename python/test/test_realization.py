import pytest

from hypy import Realization, Catchment_Area

"""
    Test suite for Realization class
"""

@pytest.fixture
def realization():
    """
        Realization object to test
    """
    id = 'realization-test'
    catchment_id = 'catchment-id'
    realization = Realization(id, catchment_id)
    yield realization

@pytest.fixture
def catchment_area():
    """
        Catchment Area object to test
    """
    id = 'catchment-area-test'
    catchment_id = 'catchment-id'
    catchment_area = Catchment_Area(id, catchment_id)
    yield catchment_area


def test_realization(realization):
    """
        Test proper construction of realization
    """
    assert realization.id == 'realization-test'

    assert realization.catchment_id == 'catchment-id'

def test_catchment_area(catchment_area):
    """
        Test proper construction of catchment_area
    """
    assert catchment_area.id == 'catchment-area-test'

    assert catchment_area.catchment_id == 'catchment-id'



