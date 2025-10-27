from cozinha.estatistica.estatistica import Estatistica

class Tabela:

    def __init__(self, estatistica: Estatistica):
        self.estatistica = estatistica

    def mostrar_tabela(self):
        print("\n=== Estatísticas Finais ===\n")

        print(f"{'':<20} {'TOTAL':<10} {'NORMAL':<10} {'PRIORITÁRIO':<10}")
        
        total_recebidos = self.estatistica.total_pedidos()
        normais_recebidos = self.estatistica.total_pedidos_recebidos_normais()
        prioritarios_recebidos = self.estatistica.total_pedidos_recebidos_prioritarios()
        print(f"{'Pedidos recebidos':<20} {total_recebidos:<10} {normais_recebidos:<10} {prioritarios_recebidos:<10}")

        total_rejeitados = self.estatistica.total_rejeitados()
        normais_rejeitados = self.estatistica.total_rejeitados_normais()
        prioritarios_rejeitados = self.estatistica.total_rejeitados_prioritarios()
        print(f"{'Pedidos rejeitados':<20} {total_rejeitados:<10} {normais_rejeitados:<10} {prioritarios_rejeitados:<10}")

        total_concluidos = self.estatistica.total_concluidos()
        normais_concluidos = self.estatistica.total_concluidos_normais()
        prioritarios_concluidos = self.estatistica.total_concluidos_prioritarios()
        print(f"{'Pedidos concluídos':<20} {total_concluidos:<10} {normais_concluidos:<10} {prioritarios_concluidos:<10}")

        print("\n--- Cozinheiros ---")
        print(f"{'Cozinheiro':<12} {'Tempo total ocioso':<20} {'Pedidos concluídos':<20}")

        pedidos = self.estatistica.pedidos_atendidos_por_cozinheiro()
        ociosidade = self.estatistica.tempo_ocioso_por_cozinheiro()

        for i in range(len(pedidos)):
            print(f"{i+1:<12} {ociosidade[i]:<20} {pedidos[i]:<20}")

        print("\nCozinheiro que mais atendeu pedidos:", self.estatistica.cozinheiro_que_mais_atendeu())
