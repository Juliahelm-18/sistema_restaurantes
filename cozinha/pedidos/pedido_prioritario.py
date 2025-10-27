from cozinha.pedidos.pedido import Pedido


class PedidoPrioritario(Pedido):

    def __init__(self, duracao_pedido: int):
        super().__init__(duracao_pedido, Pedido.TIPO_PRIORITARIO)
