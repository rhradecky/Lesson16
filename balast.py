import unittest
from main import Kalkulacka

class TestAddFunkction(unittest.TestCase):
    def test_add_intergres(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(1,2),3)

    def test_add_negative(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(-1,-1),-2)

    def test_add_float(self):
        calc = Kalkulacka()
        self.assertAlmostEqual(calc.sucet(1.1,2.2),3.3, places = 1)


    def kvadraticka_rovnica_add_intergres(self):
        calc = Kalkulacka()
        self.assertEqual(calc.kvadraticka_rovnica(1,-3,2),[5,2])

if __name__ == '__main__':
    unittest.main()






('''
import pytest
from main import Kalkulacka

def test_add_integers():
    calc = Kalkulacka()
    assert calc.sucet(1,2) == 1

def test_add_negative():
    calc = Kalkulacka()
    assert calc.sucet(-1, -1) == -2

def test_add_floats():
    calc = Kalkulacka()
    assert calc.sucet(1.1, 2.2) == pytest.approx(3.3)




import unittest
from main import Kalkulacka

class TestAddFunkction(unittest.TestCase):
    def test_add_intergres(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(1,2),3)

    def test_add_negative(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(-1,-1),-2)

    def test_add_float(self):
        calc = Kalkulacka()
        self.assertAlmostEqual(calc.sucet(1.1,2.2),3.3, places = 1)
if __name__ == '__main__':
    unittest.main()






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
    

''')
