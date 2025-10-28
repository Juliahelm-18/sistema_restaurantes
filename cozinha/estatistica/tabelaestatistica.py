# Classe para exibir a tabela de estatísticas do restaurante
from cozinha.estatistica.estatistica import Estatistica

class Tabela:

    def __init__(self, estatistica: Estatistica):
        self.estatistica = estatistica

    def mostrar_tabela(self):
        print("\n=== Estatísticas Finais ===\n")
        print("\t\t\tTOTAL\tNORMAL\tPRIORITÁRIO")
        # Utilizei \t para alinhar as colunas da tabela

        print("Pedidos recebidos\t", self.estatistica.total_pedidos(),
        "\t", self.estatistica.total_pedidos_recebidos_normais(),
        "\t", self.estatistica.total_pedidos_recebidos_prioritarios())

        print("Pedidos rejeitados\t", self.estatistica.total_rejeitados(),
        "\t", self.estatistica.total_rejeitados_normais(),
        "\t", self.estatistica.total_rejeitados_prioritarios())

        print("Pedidos concluídos\t", self.estatistica.total_concluidos(),
        "\t", self.estatistica.total_concluidos_normais(),
        "\t", self.estatistica.total_concluidos_prioritarios())

        print("\n--- Cozinheiros ---")
        print("Cozinheiro\tTempo ocioso\tPedidos concluídos")

        # Percorre cada cozinheiro mostrando seu tempo ocioso e pedidos concluídos
        # enumerate gera o índice do cozinheiro (0,1,2...) para mostrar na tabela
        # zip combina duas listas: tempos de ociosidade e pedidos atendidos
        for i, (ociosidade, pedidos) in enumerate(zip(
        self.estatistica.tempo_ocioso_por_cozinheiro(),
        self.estatistica.pedidos_atendidos_por_cozinheiro()
        )):
            print(f"{i+1}\t\t{ociosidade}\t\t{pedidos}") 
            # Utilizei i+1 para que a contagem comece em 1 e não em 0

        print("\nCozinheiro que mais atendeu pedidos:", self.estatistica.cozinheiro_que_mais_atendeu())

        while True:
            comando = input("\nDigite (V) para voltar ao menu: ").strip().upper()
            if comando == 'V':
                break
            print("Comando inválido.")
        # Fiz um loop para que o usuário possa ver a tabela antes de voltar ao menu
