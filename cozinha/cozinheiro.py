from cozinha.pedidos.pedido import Pedido


class Cozinheiro:

    def __init__(self):
        self.__pedido_atual: Pedido | None = None
        self.__pedidos_atendidos = 0
        self.__tempo_ocioso = 0

    def define_pedido_atual(self, pedido: Pedido) -> None:
        self.__pedido_atual = pedido

    def esta_disponivel(self) -> bool:
        return self.__pedido_atual is None or self.__pedido_atual.foi_concluido()

    def eh_pedido_prioritario(self) -> int:
        return self.__pedido_atual is not None and self.__pedido_atual.eh_prioritario()

    def trabalha(self) -> Pedido | None:
        """
        Consome 1 unidade de duração do pedido. Retorna o pedido concluído, se houver.
        """
        if self.__pedido_atual is None:
            self.__tempo_ocioso += 1
            return None

        self.__pedido_atual.consome_duracao()
        if self.__pedido_atual.foi_concluido():
            pedido_concluido = self.__pedido_atual
            self.__pedido_atual = None
            self.__pedidos_atendidos += 1
            return pedido_concluido
        return None

    def get_pedidos_atendidos(self) -> int:
        return self.__pedidos_atendidos

    def get_tempo_ocioso(self) -> int:
        return self.__tempo_ocioso

    def __str__(self) -> str:
        pedido = self.__pedido_atual
        return "Ocioso" if self.esta_disponivel() else str(pedido)
