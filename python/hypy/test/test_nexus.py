import pytest
from typing import Generator
from pathlib import Path
import json

from hypy import Nexus, Observation_Point

"""
    Test suite for Nexus class
"""

@pytest.fixture
def nexus():
    """
        Nexus object to test
    """
    id = 'nex-test'
    to_id = 'downstream_catchment'
    nexus = Nexus(id, to_id)
    yield nexus

@pytest.fixture
def observation_point():
    """
        Observation_Point object to test
    """
    id = 'obs-point-test'
    to_id = 'downstream_catchment'
    observation_point = Observation_Point(id, to_id)
    yield observation_point

def test_nexus(nexus):
    """
        Test proper construction of nexus
    """
    assert nexus.id == 'nex-test'

    assert nexus.to_id == 'downstream_catchment'

def test_observation_point(observation_point):
    """
        Test proper construction of observation_point
    """
    assert observation_point.id == 'obs-point-test'

    assert observation_point.to_id == 'downstream_catchment'

