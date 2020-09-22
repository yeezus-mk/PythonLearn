import pytest
from calc import line
from calc import square
from calc import cube


@pytest.mark.parametrize('a, b, answer', [
    (1, 2, [-2.0]),
    (1, -3, [3.0]),
    (1, 'Masha', [])
])
def test_line(a, b, answer, human):
    assert line(a, b) == answer


def test_lineNegative(human):
    assert line() == []

@pytest.mark.parametrize ('a, b, c , answer', [
    (1, 2, 1, [-1.0]),
    (1, 'Masha', 3, [])
])

def test_sqare(a, b, c, answer, human):
    assert square(a, b, c) == answer

def test_squareNegative(human):
    assert square() == []

@pytest.mark.parametrize('a, b, c, d, answer', [
    (0, 1, 2, 1, [-1.0]),
    ('Masha', 1, 1, 1, [])
])

def test_cube(a, b, c, d, answer, human):
    assert cube(a, b, c, d) == answer

def test_cubeNegative(human):
    assert cube() == []

