import pytest

from hypy import Realization

@pytest.fixture
def realization():
    """
        realization object to test
    """
    id = 'cat-test'
    realization = Realization(id)
    yield realization

def test_realization(realization):
    """
        Test proper construction of realization
    """
    assert realization.id == 'cat-test'
