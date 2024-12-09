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

