import pytest
import json
from pathlib import Path
from hypy import Catchment
from hypy import Nexus, HydroLocation, HydroLocationType

"""
    Test suite for Nexus class
"""

_current_dir = Path(__file__).resolve().parent

@pytest.fixture
def nexus():
    """
        Nexus object to test
    """
    nexus_id = 'nex-test'

    catchment_id_receiving0 = 'cat-hymod-receive0'
    catchment_id_receiving1 = 'cat-hymod-receive1'
    catchment_id_contributing0 = 'cat-hymod-contribute0'
    catchment_id_contributing1 = 'cat-hymod-contribute1'
    data_path = _current_dir.joinpath('data')
    data_file = data_path.joinpath('example_realization_config.json')
    with open(data_file) as fp:
        data = json.load(fp)
    params = {}

    receiving_catchments = (Catchment(catchment_id_receiving0, params), Catchment(catchment_id_receiving1, params)) #tuple

    contributing_catchments = [Catchment(catchment_id_contributing0, params), Catchment(catchment_id_contributing1, params)] #list

    location = HydroLocation(nexus_id,
                            (0,0),
                            HydroLocationType.UNDEFINED,
                            None)

    nexus = Nexus(nexus_id, location, receiving_catchments, contributing_catchments)
    receiving_catchments[0]._inflow = nexus
    receiving_catchments[1]._inflow = nexus
    contributing_catchments[0]._outflow = nexus
    contributing_catchments[1]._outflow = nexus

    yield nexus

def test_nexus(nexus):
    """
        Test proper construction of nexus
    """
    assert nexus.id == 'nex-test'

    assert nexus.receiving_catchments[0].id == 'cat-hymod-receive0'

    assert nexus.contributing_catchments[1].id == 'cat-hymod-contribute1'
