import pytest
import json
from pathlib import Path
from hypy import HydroLocation, HydroLocationType

"""
    Test suite for HydroLocation
"""

_current_dir = Path(__file__).resolve().parent

@pytest.fixture
def location():
    """
        location object to test
    """
    nexus_id = 'nex-test'
    geom = (0,0)
    type = HydroLocationType.UNDEFINED
    referenced_position = None

    location = HydroLocation(nexus_id,
                            (0,0),
                            HydroLocationType.UNDEFINED,
                            None)
    yield location

def test_hydrolocation(location):
    """
        Test proper construction of location
    """
    assert location.realized_nexus == 'nex-test'

    assert location.geometry == (0,0)

    assert location.ltype == HydroLocationType.UNDEFINED
