import unittest
from numprimos import is_primo 

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False)

    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)
        
if __name__ == "__main__":
    unittest.main()
    

    