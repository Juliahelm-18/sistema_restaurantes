import unittest
from cozinha.restaurante import Restaurante
from cozinha.estatistica.estatistica import Estatistica
from cozinha.pedidos.pedido_normal import PedidoNormal
from cozinha.pedidos.pedido_prioritario import PedidoPrioritario

class TestEstatistica(unittest.TestCase):

    def test_calculo_estatisticas(self):
        """Verifica se as estatísticas refletem corretamente os pedidos e cozinheiros."""
        restaurante = Restaurante(qtd_cozinheiros=2, limite_fila_pedidos=5)
        p1 = PedidoNormal(1)
        p2 = PedidoPrioritario(1)
        restaurante.novo_pedido(p1)
        restaurante.novo_pedido(p2)

        restaurante.executa_pedidos()
        restaurante.executa_pedidos()

        est = Estatistica(restaurante)
        self.assertEqual(est.total_pedidos(), 2)
        self.assertEqual(est.total_concluidos(), 2)
        self.assertIn(est.cozinheiro_que_mais_atendeu(), [1,2]) 

if __name__ == "__main__":
    unittest.main()
