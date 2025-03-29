import unittest


def km_a_metro(kilometros):
    return kilometros * 1000

def metro_a_pie(metros):
    return metros * 3.28084

def pulgadas_a_yarda(pulgadas):
    return pulgadas / 36

def millas_a_centimetros(millas):
    return millas * 160934.4

def milimetros_a_decimetros(milimetros):
    return milimetros / 100


class TestConversiones(unittest.TestCase):

    def test_km_a_metro(self):
        self.assertEqual(km_a_metro(5), 5000)
        self.assertEqual(km_a_metro(0), 0)
        self.assertEqual(km_a_metro(1.5), 1500)

    def test_metro_a_pie(self):
        self.assertEqual(metro_a_pie(1000), 3280.84)
        self.assertEqual(metro_a_pie(0), 0)
        self.assertAlmostEqual(metro_a_pie(10), 32.8084, places=4)

    def test_pulgadas_a_yarda(self):
        self.assertEqual(pulgadas_a_yarda(72), 2)
        self.assertEqual(pulgadas_a_yarda(0), 0)
        self.assertEqual(pulgadas_a_yarda(36), 1)

    def test_millas_a_centimetros(self):
        self.assertEqual(millas_a_centimetros(2), 321868.8)
        self.assertEqual(millas_a_centimetros(0), 0)
        self.assertEqual(millas_a_centimetros(1), 160934.4)

    def test_milimetros_a_decimetros(self):
        self.assertEqual(milimetros_a_decimetros(250), 2.5)
        self.assertEqual(milimetros_a_decimetros(0), 0)
        self.assertEqual(milimetros_a_decimetros(1000), 10)


if __name__ == "__main__":
    unittest.main()
