# Automação de cozinha comercial

Para iniciar, execute:

```bash
python main.py
```

# Relatório de Estatísticas do Restaurante
Mostra informações de pedidos e desempenho dos cozinheiros

## Pedidos
1 - Total (inclui normal e prioritário)
2 - Normal
3 - Prioritário

Há três categorias:
1 - Concluído: pedido finalizado
2 - Recebido: pedido chegou
3 - Rejeitado - pedido não pode ser atendido

## Cozinheiro
- Ocioso: tempo em que o cozinheiro ficou disponível
- Pedidos concluídos: pedidos finalizados por cada cozinheiro
- Cozinheiro que mais atendeu: cozinheiro mais produtivo

## Como usar?
- Executar o programa
- Selecione a opção de exibir a Tabela de Estatística ('T')
- Visualize os dados
- Aperte a tecla 'V' para voltar ao menu

# Testes
O projeto inclui testes automatizados para verificar se os pedidos, cozinheiros e estatísticas funcionam corretamente.

## Como executar os testes
- Abra o terminal na pasta do projeto
- Execute o comando:
```bash
   python -m unittest discover -s tests -p "*.py"
```

## Interpretando resultados
- . : teste passou com sucesso
- F : teste falhou
- E : Erro inesperado no teste

Ao final, o unittest mostra um resumo com:
- Total de testes executados.
- Número de falhas e erros, se houver.
Se todos os testes passarem, o sistema está funcionando corretamente.
