class Pedido:
    TIPO_NORMAL = "N"
    TIPO_PRIORITARIO = "P"

    qt_total_pedidos_prioritarios = 0
    qt_total_pedidos_normais = 0

    def __init__(self, duracao_pedido: int, tipo_pedido: str):
        self.__duracao_pedido = duracao_pedido
        self.__tipo_pedido = tipo_pedido

    def consome_duracao(self) -> None:
        self.__duracao_pedido -= 1

    def foi_concluido(self) -> bool:
        return self.__duracao_pedido == 0

    def duracao(self) -> int:
        return self.__duracao_pedido

    def eh_prioritario(self) -> bool:
        if self.__tipo_pedido == Pedido.TIPO_PRIORITARIO:
            Pedido.qt_total_pedidos_prioritarios += 1
        return self.__tipo_pedido == Pedido.TIPO_PRIORITARIO

    def eh_normal(self) -> bool:
        if self.__tipo_pedido == Pedido.TIPO_NORMAL:
            Pedido.qt_total_pedidos_normais += 1
        return self.__tipo_pedido == Pedido.TIPO_NORMAL

    def __str__(self) -> str:
        return f"{self.__duracao_pedido}{self.__tipo_pedido}"
