# Classe que representa o restaurante
# Gerencia cozinheiros, filas de pedidos e estatísticas de atendimento
# Também controla limites de fila e pedidos prioritários
from cozinha.cozinheiro import Cozinheiro
from cozinha.pedidos.pedido import Pedido
from cozinha.pedidos.pedido_normal import PedidoNormal
from cozinha.utils.queue import Queue


class Restaurante:
    def __init__(self, qtd_cozinheiros: int, limite_fila_pedidos: int, limite_prioritario_turno: int = 2):
        self.qtd_cozinheiros = qtd_cozinheiros
        self.cozinheiros = [Cozinheiro() for _ in range(self.qtd_cozinheiros)]
        self.limite_fila_pedidos = limite_fila_pedidos

        self.contador_pedidos_recebidos = 0
        self.contador_pedidos_rejeitados = 0
        self.contador_pedidos_rejeitados_prioritarios = 0
        self.contador_pedidos_rejeitados_normais = 0
        self.contador_pedidos_concluidos = 0
        self.contador_pedidos_concluidos_prioritarios = 0
        self.contador_pedidos_concluidos_normais = 0

        self.fila_pedidos_normais = Queue()
        self.fila_pedidos_prioritarios = Queue()

        self.limite_prioritario_turno = limite_prioritario_turno

    def qtd_pedidos_em_andamento(self) -> int:
        return self.fila_pedidos_prioritarios.queue_length() + self.fila_pedidos_normais.queue_length()

    def __novo_pedido(self, fila: Queue, pedido: Pedido) -> None:
        self.contador_pedidos_recebidos += 1
        if self.pode_receber_pedido():
            fila.enqueue(pedido)
        else:
            if pedido.tipo() == Pedido.TIPO_PRIORITARIO:
                self.contador_pedidos_rejeitados_prioritarios += 1
            else:
                self.contador_pedidos_rejeitados_normais += 1
            self.contador_pedidos_rejeitados += 1

    def novo_pedido(self, pedido: Pedido) -> None:
        if isinstance(pedido, PedidoNormal):
            fila = self.fila_pedidos_normais
        else:
            fila = self.fila_pedidos_prioritarios
        self.__novo_pedido(fila, pedido)

    def pode_receber_pedido(self) -> bool:
        return self.qtd_pedidos_em_andamento() < self.limite_fila_pedidos

    def executa_pedidos(self) -> None:
        for idx in range(len(self.cozinheiros)):
            cozinheiro = self.cozinheiros[idx]
            if cozinheiro.esta_disponivel():
                if self.ha_prioritarios_na_fila() and self.pode_iniciar_prioritario():
                    cozinheiro.define_pedido_atual(self.fila_pedidos_prioritarios.dequeue())
                elif self.ha_normais_na_fila():
                    cozinheiro.define_pedido_atual(self.fila_pedidos_normais.dequeue())
            else:
                pedido_concluido = cozinheiro.trabalha()
                if pedido_concluido:  
                    self.contador_pedidos_concluidos += 1
                    if pedido_concluido.eh_prioritario():
                        self.contador_pedidos_concluidos_prioritarios += 1
                    else:
                        self.contador_pedidos_concluidos_normais += 1


    def pode_iniciar_prioritario(self) -> bool:
        return (
                self.get_qtd_prioritarios_em_andamento() < self.limite_prioritario_turno
        ) or not self.ha_normais_na_fila()

    def __ha_pedido(self, fila_pedidos: Queue) -> bool:
        return fila_pedidos.queue_length() > 0

    def ha_normais_na_fila(self) -> bool:
        return self.__ha_pedido(self.fila_pedidos_normais)

    def ha_prioritarios_na_fila(self) -> bool:
        return self.__ha_pedido(self.fila_pedidos_prioritarios)

    def imprimir_status(self) -> None:
        print('Fila pedidos normais: ', self.fila_pedidos_normais)
        print('Fila pedidos prioritários: ', self.fila_pedidos_prioritarios)
        print('---')
        print('Cozinheiros:', [str(x) for x in self.cozinheiros])
        fila_em_uso = self.qtd_pedidos_em_andamento()
        print(f'Limite fila pedidos: {fila_em_uso}/{self.limite_fila_pedidos}')
        print('---')
        print('Pedidos recebidos: ', self.contador_pedidos_recebidos)
        print('Pedidos rejeitados: ', self.contador_pedidos_rejeitados)
        print('Pedidos concluidos: ', self.contador_pedidos_concluidos)

    def get_qtd_prioritarios_em_andamento(self):
        return sum([1 if x.eh_pedido_prioritario() else 0 for x in self.cozinheiros])
