import pytest

from hypy import Nexus

@pytest.fixture
def nexus():
    """
        Nexus object to test
    """
    id = 'nex-test'
    nexus = Nexus(id)
    yield nexus

def test_nexus(nexus):
    """
        Test proper construction of nexus
    """
    assert nexus.id == 'nex-test'
