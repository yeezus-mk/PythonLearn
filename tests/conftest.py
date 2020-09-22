import pytest
import people.Human as Human

@pytest.fixture
def human():
    return Human()


