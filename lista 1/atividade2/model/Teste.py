
import unittest
from Pessoa import Pessoa


class TestePessoa(unittest.TestCase):

    def test_feminino_abaixo_do_peso(self):
        self.assertEqual(
            Pessoa("F", 19.0, 1.0).calcularImc(),
            "abaixo do peso"
        )

    def test_feminino_fronteira_19_1(self):
        self.assertEqual(
            Pessoa("F", 19.1, 1.0).calcularImc(),
            "no peso normal"
        )

    def test_feminino_fronteira_25_8(self):
        self.assertEqual(
            Pessoa("F", 25.8, 1.0).calcularImc(),
            "marginalmente acima do peso"
        )

    def test_feminino_fronteira_27_3(self):
        self.assertEqual(
            Pessoa("F", 27.3, 1.0).calcularImc(),
            "acima do peso ideal"
        )

    def test_feminino_fronteira_32_3(self):
        self.assertEqual(
            Pessoa("F", 32.3, 1.0).calcularImc(),
            "obeso"
        )

    def test_masculino_abaixo_do_peso(self):
        self.assertEqual(
            Pessoa("M", 20.6, 1.0).calcularImc(),
            "abaixo do peso"
        )

    def test_masculino_fronteira_20_7(self):
        self.assertEqual(
            Pessoa("M", 20.7, 1.0).calcularImc(),
            "no peso normal"
        )

    def test_masculino_fronteira_26_4(self):
        self.assertEqual(
            Pessoa("M", 26.4, 1.0).calcularImc(),
            "marginalmente acima do peso"
        )

    def test_masculino_fronteira_27_8(self):
        self.assertEqual(
            Pessoa("M", 27.8, 1.0).calcularImc(),
            "acima do peso ideal"
        )

    def test_masculino_fronteira_31_1(self):
        self.assertEqual(
            Pessoa("M", 31.1, 1.0).calcularImc(),
            "obeso"
        )


if __name__ == "__main__":
    unittest.main()
