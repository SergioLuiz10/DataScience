
Olá! Este é um projeto desenvolvido para análise exploratória de dados de filmes e avaliações. Aqui, eu carrego, organizo e analiso dois conjuntos de dados: um com as avaliações de filmes e outro com informações sobre os filmes. Utilizo bibliotecas do Python para manipular os dados e gerar visualizações gráficas que ajudam a entender as distribuições das notas.

Tecnologias Utilizadas
Python: Linguagem de programação base do projeto.
Pandas: Para manipulação e análise de dados tabulares.
Matplotlib: Para visualização gráfica dos dados.
Funcionalidades
Leitura e organização dos dados:

Carrego os dados de avaliações e os dados de filmes de arquivos CSV hospedados online.
Renomeio as colunas para facilitar o entendimento e a manipulação dos dados.
Análise das notas dos filmes:

Exibo um histograma para visualizar a distribuição das notas dadas aos filmes.
Calculo e apresento estatísticas importantes como a média, mediana e outras descrições gerais das notas.
Média de notas para filmes específicos:

Extraio e apresento a média de notas de filmes específicos, como Toy Story e Jumanji.
Média das notas para todos os filmes:

Uso o groupby para calcular a média de notas de todos os filmes, evitando fazer esse processo manualmente para cada filme.
Exibo um histograma com a distribuição dessas médias.
Como Executar
Certifique-se de ter o Python instalado em sua máquina.
Instale as bibliotecas necessárias usando:
bash
Copiar código
pip install pandas matplotlib
Execute o código em um ambiente Python (por exemplo, Jupyter Notebook ou diretamente no terminal).
