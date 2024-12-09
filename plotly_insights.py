import pandas as pd  # Nome comum para pandas.

# Leitura do arquivo CSV com dados de cancelamentos.
tabela = pd.read_csv("cancelamentos_sample.csv")

# Remover a coluna "CustomerID" que não é relevante para a análise.
tabela = tabela.drop(columns="CustomerID")
print(tabela)
# Exibir informações sobre a tabela, como tipos de dados e valores ausentes.
print(tabela.info())

# Remover linhas com valores ausentes para garantir integridade dos dados.
tabela = tabela.dropna()
print(tabela.info())

# Contar o número de clientes que cancelaram e que não cancelaram.
print(tabela["cancelou"].value_counts())

# Calcular a proporção de cancelamentos em relação ao total.
print(tabela["cancelou"].value_counts(normalize=True))

# Formatar a proporção como porcentagem.
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

import plotly.express as px

# Gerar gráficos interativos para cada coluna da tabela.
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()  # Os gráficos serão abertos no navegador.
    

    # Insights obtidos a partir da análise inicial:
# 1. Clientes que ligaram mais de 4 vezes para o call center cancelaram.
#    Proposta: Implementar um processo interno para resolver problemas em até 2 ligações.
# 2. Clientes com mais de 20 dias de atraso no pagamento cancelaram.
#    Proposta: Criar alertas para contatar clientes ao atingir 10 dias de atraso.
# 3. Clientes com contratos mensais tiveram maior índice de cancelamento.
#    Proposta: Oferecer descontos para contratos anuais ou trimestrais.

# Aplicando filtros para simular o impacto das melhorias propostas:
# Resolvendo problemas no call center (clientes que ligaram até 4 vezes).
filtro = tabela["ligacoes_callcenter"] <= 4
tabela = tabela[filtro]

# Resolvendo atrasos de pagamento (clientes com até 20 dias de atraso).
filtro = tabela["dias_atraso"] <= 20
tabela = tabela[filtro]

# Resolvendo o problema de contratos mensais (excluindo contratos mensais).
filtro = tabela["duracao_contrato"] != "Monthly"
tabela = tabela[filtro]

