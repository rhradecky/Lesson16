import pytest
from main import Kalkulacka

@pytest.mark.parametrize("a,b, expected", [
    (1,2,3),
    (4,5,9),
    (10,-2,8),
    (0,0,0),
    (-1,-1,-2),
])

def test_add(a,b,expected):
    calc = Kalkulacka()
    assert calc.sucet(a,b) == expected

