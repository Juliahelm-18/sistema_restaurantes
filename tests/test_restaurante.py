import unittest
from cozinha.restaurante import Restaurante
from cozinha.pedidos.pedido_normal import PedidoNormal
from cozinha.pedidos.pedido_prioritario import PedidoPrioritario

class TestRestaurante(unittest.TestCase):
    def setUp(self):
        self.restaurante = Restaurante(qtd_cozinheiros=2, limite_fila_pedidos=3)

    def test_pode_receber_pedido(self):
        self.assertTrue(self.restaurante.pode_receber_pedido())

    def test_novo_pedido_normal(self):
        pedido = PedidoNormal(duracao_pedido=5)
        self.restaurante.novo_pedido(pedido)
        self.assertEqual(self.restaurante.contador_pedidos_recebidos, 1)
        self.assertEqual(self.restaurante.fila_pedidos_normais.queue_length(), 1)

    def test_rejeicao_de_pedido_quando_fila_cheia(self):
        self.restaurante.limite_fila_pedidos = 0
        pedido = PedidoNormal(duracao_pedido=5)
        self.restaurante.novo_pedido(pedido)
        self.assertEqual(self.restaurante.contador_pedidos_rejeitados, 1)

    def test_executa_pedidos_prioritario_primeiro(self):
        pedido1 = PedidoPrioritario(duracao_pedido=3)
        pedido2 = PedidoNormal(duracao_pedido=5)
        self.restaurante.novo_pedido(pedido1)
        self.restaurante.novo_pedido(pedido2)
        self.restaurante.executa_pedidos()
        # Deve ter atribuído o prioritário a algum cozinheiro
        self.assertTrue(any(c.eh_pedido_prioritario() for c in self.restaurante.cozinheiros))

if __name__ == '__main__':
    unittest.main()
