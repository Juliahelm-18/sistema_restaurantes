from cozinha.estatistica.estatistica import Estatistica
from cozinha.estatistica.tabelaestatistica import Tabela
from cozinha.pedidos.pedido_normal import PedidoNormal
from cozinha.pedidos.pedido_prioritario import PedidoPrioritario
from cozinha.restaurante import Restaurante
from cozinha.utils.utils import Utils


class Programa:
    CMD_SAIR = 'S'
    CMD_EXECUTAR = 'E'
    CMD_PEDIDO_PRIORITARIO = 'P'
    CMD_PEDIDO_NORMAL = 'N'
    CMD_TABELA = 'T' 
    OPCOES_COMANDOS = [CMD_PEDIDO_NORMAL, CMD_PEDIDO_PRIORITARIO, CMD_EXECUTAR, CMD_SAIR, CMD_TABELA]

    def iniciar(self) -> None:
        Utils.clear_screen()

        qtd_cozinheiros = self.obter_cozinheiro()
        limite_fila_pedidos = self.obter_tamanho_fila()
        restaurante = Restaurante(qtd_cozinheiros, limite_fila_pedidos)
        estatistica = Estatistica(restaurante)
        tabela = Tabela(estatistica)

        Utils.clear_screen()

        while True:
            Utils.clear_screen()
            restaurante.imprimir_status()

            comando = self.obter_acao()
            if comando == self.CMD_EXECUTAR:
                restaurante.executa_pedidos()
            elif comando == self.CMD_PEDIDO_NORMAL:
                duracao = self.obter_duracao_pedido()
                restaurante.novo_pedido(PedidoNormal(duracao))
            elif comando == self.CMD_PEDIDO_PRIORITARIO:
                duracao = self.obter_duracao_pedido()
                restaurante.novo_pedido(PedidoPrioritario(duracao))
            elif comando == self.CMD_TABELA: 
                tabela.mostrar_tabela()
                break

    def obter_int_value(self, msg: str) -> int:
        while True:
            try:
                valor = int(input(msg))
            except ValueError:
                valor = 0
            if valor <= 0:
                print('Valor inválido (deve ser >0)')
            else:
                return valor

    def obter_tamanho_fila(self) -> int:
        return self.obter_int_value('Digite o limite da fila de pedidos: ')

    def obter_cozinheiro(self) -> int:
        return self.obter_int_value('Digite a quantidade de cozinheiros: ')

    def obter_duracao_pedido(self) -> int:
        return self.obter_int_value('Digite a duração do pedido: ')

    def obter_acao(self) -> str:
        print('\n')
        while True:
            comando = input('Ações disponíveis:'
                            '\n\tPedido (N)ormal'
                            '\n\tPedido (P)rioritário'
                            '\n\t(E)xecutar pedidos'
                            '\n\t(T)abela de estatísticas'
                            '\n\t(S)air'
                            '\nDigite a ação: ')
            comando = comando.upper()
            if comando not in self.OPCOES_COMANDOS:
                print('Comando inválido, tente novamente')
            else:
                return comando
