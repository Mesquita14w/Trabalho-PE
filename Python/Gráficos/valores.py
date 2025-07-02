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
