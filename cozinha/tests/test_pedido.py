import unittest
from cozinha.pedidos.pedido import Pedido

class TestPedido(unittest.TestCase):

    def test_criacao_pedido_normal(self):
        """Verifica se um pedido normal é criado corretamente."""
        pedido = Pedido(3, Pedido.TIPO_NORMAL)
        self.assertEqual(pedido.duracao(), 3)
        self.assertTrue(pedido.eh_normal())
        self.assertFalse(pedido.eh_prioritario())

    def test_conclusao_pedido(self):
        """Verifica se a duração do pedido decrementa corretamente e conclui."""
        pedido = Pedido(2, Pedido.TIPO_PRIORITARIO)
        self.assertFalse(pedido.foi_concluido())
        pedido.consome_duracao()
        self.assertFalse(pedido.foi_concluido())
        pedido.consome_duracao()
        self.assertTrue(pedido.foi_concluido())

if __name__ == "__main__":
    unittest.main()
