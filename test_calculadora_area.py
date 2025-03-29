import unittest
import math

# Funciones de cálculo de área
def area_cuadrado(lado):
    return lado ** 2

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rectangulo(base, altura):
    return base * altura

def area_hexagono(lado):
    return (3 * math.sqrt(3) * lado ** 2) / 2

# Clase para las pruebas unitarias
class TestCalculadoraArea(unittest.TestCase):

    def test_area_cuadrado(self):
        self.assertEqual(area_cuadrado(4), 16)
        self.assertEqual(area_cuadrado(0), 0)
        self.assertEqual(area_cuadrado(5.5), 30.25)

    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(1), math.pi, places=5)
        self.assertAlmostEqual(area_circulo(0), 0, places=5)
        self.assertAlmostEqual(area_circulo(2), math.pi * 4, places=5)

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(5, 10), 25)
        self.assertEqual(area_triangulo(0, 10), 0)
        self.assertEqual(area_triangulo(6, 3), 9)

    def test_area_rectangulo(self):
        self.assertEqual(area_rectangulo(5, 10), 50)
        self.assertEqual(area_rectangulo(0, 10), 0)
        self.assertEqual(area_rectangulo(3.5, 2), 7)

    def test_area_hexagono(self):
        self.assertAlmostEqual(area_hexagono(4), (3 * math.sqrt(3) * 4 ** 2) / 2, places=5)
        self.assertEqual(area_hexagono(0), 0)
        self.assertAlmostEqual(area_hexagono(6), (3 * math.sqrt(3) * 6 ** 2) / 2, places=5)

if __name__ == '__main__':
    unittest.main()
