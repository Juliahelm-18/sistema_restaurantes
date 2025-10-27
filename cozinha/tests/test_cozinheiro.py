import unittest
from cozinha.cozinheiro import Cozinheiro
from cozinha.pedidos.pedido import Pedido

class TestCozinheiro(unittest.TestCase):

    def test_trabalha_com_pedido(self):
        """Verifica se o cozinheiro trabalha corretamente e conta pedidos atendidos e tempo ocioso."""
        cozinheiro = Cozinheiro()
        pedido = Pedido(2, Pedido.TIPO_NORMAL)

        cozinheiro.define_pedido_atual(pedido)
        self.assertFalse(cozinheiro.esta_disponivel())


        self.assertIsNone(cozinheiro.trabalha())
        self.assertFalse(pedido.foi_concluido())


        concluido = cozinheiro.trabalha()
        self.assertTrue(pedido.foi_concluido())
        self.assertEqual(concluido, pedido)
        self.assertEqual(cozinheiro.get_pedidos_atendidos(), 1)

if __name__ == "__main__":
    unittest.main()
