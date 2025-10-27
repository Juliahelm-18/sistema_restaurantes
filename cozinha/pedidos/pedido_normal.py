from cozinha.pedidos.pedido import Pedido


class PedidoNormal(Pedido):

    def __init__(self, duracao_pedido: int):
        super().__init__(duracao_pedido, Pedido.TIPO_NORMAL)
