import pytest
import json
import pandas as pd
import datetime as dt
from pathlib import Path
from hypy import NWISLocation, HydroLocationType

"""
    Test suite for NWISLocation
"""

_current_dir = Path(__file__).resolve().parent

@pytest.fixture
def location():
    """
        nwis location object to test
    """
    station_id = 'not-a-real-station'
    nexus_id = 'nex-test'
    geom = (0,0)
    referenced_position = None

    location = NWISLocation(station_id, nexus_id,
                            (0,0),
                            None)
    yield location

@pytest.fixture
def real_nwis():
    """
        A real NWIS connection
    """
    station_id = '02146211'
    nexus_id = 'nex-test'
    geom = (0,0)

    location = NWISLocation(station_id, nexus_id, geom)

    yield location

def test_get_data(real_nwis):
    """
        Connect to a real nwis station via nwis client
    """
    data = real_nwis.get_data()
    print(data)
    assert data is not None

def test_get_data_1(real_nwis):
    """
        Connect to a nwis and get a range of data
    """

    end = pd.Timestamp.now().floor('h')
    start = end - dt.timedelta(weeks=1)
    data = real_nwis.get_data(start, end)
    print(data)
    assert data is not None
    #Should minimally have hourly data, but maybe up to 5 min resolution
    assert len(data) >= 7*24 + 1
    assert len(data) <= 7*( 24*(60/5) ) + 1 #+1 for inclusive range

def test_nwislocation(location):
    """
        Test proper construction of location
    """
    assert location.station_id == 'not-a-real-station'
    assert location.realized_nexus == 'nex-test'

    assert location.geometry == (0,0)

    assert location.ltype == HydroLocationType.hydrometricStation
