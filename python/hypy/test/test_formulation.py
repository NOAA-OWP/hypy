import pytest

from hypy import Formulation

@pytest.fixture
def formulation():
    """
        Nexus object to test
    """
    id = 'cat-test'
    formulation = Formulation(id)
    yield formulation

def test_formulation(formulation):
    """
        Test proper construction of formulation
    """
    assert formulation.id == 'cat-test'
