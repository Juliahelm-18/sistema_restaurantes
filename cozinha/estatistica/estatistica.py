from cozinha.restaurante import Restaurante
from cozinha.pedidos.pedido_normal import PedidoNormal
from cozinha.pedidos.pedido_prioritario import PedidoPrioritario
from cozinha.pedidos.pedido import Pedido

class Estatistica:

    def __init__(self, restaurante: Restaurante):
        self.restaurante = restaurante

    def total_pedidos_recebidos_prioritarios(self) -> int:
        return Pedido.qt_total_pedidos_prioritarios

    def total_pedidos_recebidos_normais(self) -> int:
        return Pedido.qt_total_pedidos_normais
    
    def total_pedidos(self) -> int:
        return (Pedido.qt_total_pedidos_normais +
                Pedido.qt_total_pedidos_prioritarios)
    
    def total_rejeitados_prioritarios(self) -> int:
        return self.restaurante.contador_pedidos_rejeitados_prioritarios

    def total_rejeitados_normais(self) -> int:
        return self.restaurante.contador_pedidos_rejeitados_normais

    def total_rejeitados(self) -> int:
        return self.restaurante.contador_pedidos_rejeitados

    def total_concluidos_prioritarios(self) -> int:
        return self.restaurante.contador_pedidos_concluidos_prioritarios

    def total_concluidos_normais(self) -> int:
        return self.restaurante.contador_pedidos_concluidos_normais

    def total_concluidos(self) -> int:
        return self.restaurante.contador_pedidos_concluidos
    
    def pedidos_atendidos_por_cozinheiro(self):
        lista = []
        for c in self.restaurante.cozinheiros:
            lista.append(c.get_pedidos_atendidos())
        return lista

    def tempo_ocioso_por_cozinheiro(self):
        lista = []
        for c in self.restaurante.cozinheiros:
            lista.append(c.get_tempo_ocioso())
        return lista

    def cozinheiro_que_mais_atendeu(self):
        atendimentos = self.pedidos_atendidos_por_cozinheiro()
        if len(atendimentos) == 0:
            return None
        maior = max(atendimentos)
        return atendimentos.index(maior) + 1