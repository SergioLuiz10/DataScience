import pandas as pd 
import matplotlib.pyplot as plt

# Carregando e renomeando colunas do DataFrame de notas
dadosNotas = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv")
dadosNotas.columns = ["usuarioId", "filmeId", "nota", "dataNota"]

# Exibindo histograma das notas
dadosNotas["nota"].plot(kind='hist')
plt.show()

# Calculando estatísticas das notas
medianaRepartir = dadosNotas["nota"].median()
media = dadosNotas["nota"].mean()
print("A mediana é:", medianaRepartir)
print("A média é:", media)
print(dadosNotas["nota"].describe())

# Carregando o DataFrame de filmes
dadosfilme = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/movies.csv")
dadosfilme.columns = ["filmeId", "titulo", "genero"]

# Filtrando dados de um filme específico
print(dadosNotas.query("filmeId == 1")["nota"].mean()) #media do primeiro filme toystory
print(dadosNotas.query("filmeId == 2")["nota"].mean())   #media do segundo jumanji

#pra não precisar fazer na mao usar a blibioteca groupby
medias_filmes = dadosNotas.groupby("filmeId")["nota"].mean()
medias_filmes.plot(kind='hist')
plt.show()
