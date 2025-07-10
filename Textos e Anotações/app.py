import seaborn as sns
import matplotlib.pyplot as plt

# Dados
meses = ['Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
vendas = [190, 210, 180, 200, 195, 220]

# Configurando o tema
sns.set_theme(style='darkgrid')

# Criando o gráfico de linha com Seaborn
plt.figure(figsize=(10, 6),dpi=150) 
sns.lineplot(x=meses, y=vendas)

# Adicionando título e legendas aos eixos
plt.title('Vendas Mensais', fontsize=16)
plt.xlabel('Meses', fontsize=14)
plt.ylabel('Vendas', fontsize=14)

# Como adicionar texto usando Matplotlib
plt.text(28, 178.5, "Pior Mês", fontsize=10, color='red')
plt.text(57, 220, "Melhor Mês", fontsize=10, color='green', backgroundcolor='black')

# Exibindo o gráfico
plt.show()

# Neste exemplo, usamos Seaborn para criar o gráfico de linha por ser mais direto e oferecer uma estética melhorada com menos código.
# Após criar o gráfico com Seaborn, usamos funções do Matplotlib para adicionar textos personalizados ao gráfico,
# permitindo destacar informações específicas como o pior e o melhor mês em termos de vendas.
