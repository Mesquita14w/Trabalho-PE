# IMPORTANDO AS BIBLIOTECAS:

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


# IMPORTANDO O DATASET:

dsl = '/...'
df = pd.read_csv(dsl)
df


# REALIZANDO A REGRESSÃO:

# Definindo as Variáveis X e Y:
df.columns = df.columns.str.strip()
X = df[["Área (m²)", "Quartos", "Distância Centro (km)", "Idade (anos)"]]
y = df["Preço Aluguel (R$)"]

# Adicionando uma constante para o intercepto β
X = sm.add_constant(X)

# Ajustando o modelo de regressão
modelo = sm.OLS(y, X).fit()

# Exibindo o resumo do modelo
print(modelo.summary())

# OBS: OS CÓDIGOS PARA CONSTRUIR OS GRÁFICOS ESTÃO DISPONÍVEIS NA PASTA GRÁFICOS NESTE MESMO DIRETÓRIO.
