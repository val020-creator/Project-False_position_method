"""
Pruebas Unitarias para el Motor Matemático de Falsa Posición
Verificación de casos obligatorios según especificaciones del proyecto.
"""

import unittest
from falsaposicion import falsa_posicion

class TestFalsaPosicion(unittest.TestCase):
    
    def test_caso_principal_proyecto(self):
        # f(x) = x^3 - 3x - 1 en [1, 2], tolerancia 0.05%
        func = "x**3 - 3*x - 1"
        iters, res, msg = falsa_posicion(func, 1.0, 2.0, tol=0.05)
        self.assertEqual(len(iters), 4)
        self.assertAlmostEqual(res, 1.879303, places=5)
        self.assertLessEqual(iters[-1]["error"], 0.05)

    def test_intervalo_sin_cambio_de_signo(self):
        # f(x) = x^2 + 1 en [1, 2] -> f(1)=2, f(2)=5 (sin cambio de signo)
        func = "x**2 + 1"
        with self.assertRaises(ValueError):
            falsa_posicion(func, 1.0, 2.0)

    def test_raiz_exacta_extremo(self):
        # f(x) = x - 2 en [1, 2] -> f(2) = 0
        func = "x - 2"
        iters, res, msg = falsa_posicion(func, 1.0, 2.0)
        self.assertEqual(res, 2.0)

    def test_intervalo_invalido(self):
        func = "x**3 - 3*x - 1"
        with self.assertRaises(ValueError):
            falsa_posicion(func, 2.0, 1.0) # a > b

if __name__ == "__main__":
    unittest.main()
