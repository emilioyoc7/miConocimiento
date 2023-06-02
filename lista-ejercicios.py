import unittest

def suma(uno,dos):
    total = uno + dos
    return total

class pruebas(unittest.TestCase):
    def tets_suma(self):
        self.assertEqual(suma(1,2),3)

if __name__ == "__main__":
    unittest.main()