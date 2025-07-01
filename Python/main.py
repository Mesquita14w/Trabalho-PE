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


# GRÁFICOS DE RESÍDUOS VS VALORES PREDITOS:

y_pred = modelo.predict(X)
residuos = y - y_pred

plt.figure(figsize=(10,6))
sns.scatterplot(x=y_pred, y=residuos)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Valores preditos")
plt.ylabel("Resíduos")
plt.title("Resíduos vs Valores Preditos")
plt.grid(True)
plt.show()


# HISTOGRAMA DE RESÍDUOS:

plt.figure(figsize=(10,6))
sns.histplot(residuos, kde=True, bins=15, color='purple')
plt.xlabel("Resíduos")
plt.title("Distribuição dos Resíduos")
plt.grid(True)
plt.show()
