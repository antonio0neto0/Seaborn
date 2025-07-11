import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dados para gráfico de Barra
x_bar = ['A', 'B', 'C', 'D', 'E']
y_bar = [10, 24, 36, 40, 15]
df_bar = pd.DataFrame({'X': x_bar, 'Y': y_bar})

# Dados para gráfico de Linha
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)
df_line = pd.DataFrame({'X': x_line, 'Y': y_line})

# Dados para gráfico de Dispersão
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
df_scatter = pd.DataFrame({'X': x_scatter, 'Y': y_scatter})

# Dados para gráfico de Linha
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
vendas = [150, 200, 170, 180, 160, 175]
df_vendas = pd.DataFrame({'Meses': meses, 'Vendas': vendas})

plt.figure(figsize=(10,10))
sns.barplot(x='X', y='Y', data=df_bar,hue='X', palette='bright')
plt.title('Gráfico de Barra')
plt.show()

# Gráfico de Linha
sns.lineplot(x='X', y='Y', data=df_line, color='red')
plt.title('Gráfico de Linha')
plt.show()

# Gráfico de Dispersão
sns.scatterplot(x='X', y='Y', data=df_scatter, color='blue', alpha=0.5)
plt.title('Gráfico de Dispersão')
plt.show()

# Gráfico de Vendas Mensais
sns.lineplot(x='Meses', y='Vendas', data=df_vendas, marker='o', linestyle='--', color='green', label='Vendas Mensais')
plt.title('Vendas Mensais no Primeiro Semestre')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.legend(title='Legenda', loc='upper right')
plt.show()

