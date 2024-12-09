import pandas as pd  # Nome comum para pandas

# Leitura do arquivo CSV com dados de cancelamentos
tabela = pd.read_csv("cancelamentos_sample.csv")

# Remover a coluna "CustomerID" que não é relevante para a análise
tabela = tabela.drop(columns="CustomerID")
print(tabela)
# Exibir informações sobre a tabela, como tipos de dados e valores ausentes
print(tabela.info())

# Remover linhas com valores ausentes para garantir integridade dos dados
tabela = tabela.dropna()
print(tabela.info())

# Contar o número de clientes que cancelaram e que não cancelaram
print(tabela["cancelou"].value_counts())

# Calcular a proporção de cancelamentos em relação ao total
print(tabela["cancelou"].value_counts(normalize=True))

# Formatar a proporção como porcentagem
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

import plotly.express as px

# Gerar gráficos interativos para cada coluna da tabela
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()  # Os gráficos serão abertos no navegador

