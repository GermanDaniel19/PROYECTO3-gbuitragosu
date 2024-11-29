import unittest
from models.producto import Producto

class TestProducto(unittest.TestCase):
        
    def test_vender_should_return_ok(self):
        producto = Producto()
        self.assertIsInstance(producto.vender(1),str)

    def test_producto_rentable_should_return_ok(self):
        producto = Producto()
        self.assertIsNone(producto.producto_rentable())