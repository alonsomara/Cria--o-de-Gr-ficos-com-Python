import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

#Histograma - Distribuição do preço dos produtos
plt.hist(df['Preço'], bins=30, alpha=0.8)
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.title('Distribuição dos Preços dos Produtos')
plt.show()

#Dispersão - Preço x Quantidade vendida
plt.scatter(df['Preço'], df['Qtd_Vendidos'])
plt.title('Dispersão - Preço x Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()

#Mapa de Calor - Correlação entre preço, quantidade de vendidos e número de avaliações
corr = df[['Preço', 'Qtd_Vendidos_Cod', 'N_Avaliações_MinMax']].corr()
plt.subplot(2, 2, 3) #1 linha, 2 colunas, terceiro gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Preço, Quantidade Vendida, Número de Avaliações')

plt.tight_layout() #ajustar espaçamentos
plt.show()

#Gráfico de Barras - Quantidade de Temporada
plt.figure(figsize=(10,6))
df['Temporada_Cod'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Quantidade de temporadas')
plt.xlabel('Temporada')
plt.ylabel('Contagem')
plt.tight_layout()
plt.show()

#Gráfico de Pizza - Distribuição da Marca Keeper por gênero
marca_escolhida = 'keeper'

df[df['Marca'] == marca_escolhida]['Gênero'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title(f'Distribuição de Gênero – Marca {marca_escolhida}')
plt.ylabel('')
plt.show()

#Gráfico de Densidade - Preço
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'], fill=True)
plt.title('Densidade dos Preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.show()

#Gráfico de regressão - Preço x Quantidade Vendida
sns.regplot(x='Preço', y='Qtd_Vendidos_Cod', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regressão de preço e quantidade vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()

