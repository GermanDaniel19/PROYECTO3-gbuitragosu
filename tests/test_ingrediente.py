import unittest
from models.ingrediente import Ingrediente

class TestIngrediente(unittest.TestCase):

    def test_es_sano_should_return_ok(self):
        ingrediente = Ingrediente()
        self.assertIsInstance(ingrediente.es_sano(1),str)

    def test_bajar_complemento_should_return_ok(self):
        ingrediente = Ingrediente()
        self.assertIsInstance(ingrediente.bajar_complemento(4),str)

    def test_reabastecer_should_return_ok(self):
        ingrediente = Ingrediente()
        self.assertIsInstance(ingrediente.reabastecer(4),str)

