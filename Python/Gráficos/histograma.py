# HISTOGRAMA DOS RESÍDUOS:

plt.figure(figsize=(10,6))
sns.histplot(residuos, kde=True, bins=15, color='purple')
plt.xlabel("Resíduos")
plt.title("Distribuição dos Resíduos")
plt.grid(True)
plt.show()
