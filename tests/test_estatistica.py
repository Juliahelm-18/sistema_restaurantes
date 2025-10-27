import unittest
from cozinha.pedidos.pedido import Pedido
from cozinha.restaurante import Restaurante
from cozinha.estatistica.estatistica import Estatistica
from cozinha.pedidos.pedido_normal import PedidoNormal
from cozinha.pedidos.pedido_prioritario import PedidoPrioritario

class TestEstatistica(unittest.TestCase):

    def setUp(self):
        Pedido.qt_total_pedidos_normais = 0
        Pedido.qt_total_pedidos_prioritarios = 0

        self.restaurante = Restaurante(qtd_cozinheiros=2, limite_fila_pedidos=5)
        
        self.estatistica = Estatistica(self.restaurante)

    def test_calculo_estatisticas(self):
        """Verifica se as estatísticas refletem corretamente os pedidos e cozinheiros."""
        p1 = PedidoNormal(1)
        p2 = PedidoPrioritario(1)
        self.restaurante.novo_pedido(p1)
        self.restaurante.novo_pedido(p2)

        self.restaurante.executa_pedidos()
        self.restaurante.executa_pedidos()

        est = Estatistica(self.restaurante)
        self.assertEqual(est.total_pedidos(), 2)
        self.assertEqual(est.total_concluidos(), 2)
        self.assertIn(est.cozinheiro_que_mais_atendeu(), [1,2]) 

if __name__ == "__main__":
    unittest.main()
