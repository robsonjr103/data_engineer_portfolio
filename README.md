#  Meu portfolio de projetos de Engenharia de Dados

## Nesse repositório estão armazenados todos os meus projetos desenvolvidos na minha jornada para me tornar um Engenheiro de Dados.

## Uma breve explicação de cada projeto:

### Análise do conjunto de dados da empresa ficticia House Rocket (house_rocket_analysis):

> Nesse projeto eu faço uma análise no conjunto de dados com mais de 21.000 casas disponíveis para compra da empresa ficticia House Rocket, que trabalha com a compra e re-venda de casas. Eu repondo 4 perguntas principais do "CEO" da House Rocket, como: "Quais casas deveriamos comprar?", "Qual o melhor preço para re-venda e quando vende-las?", "Vale a pena reformar as casas antes de vende-las?". Além disso também há uma Aplicação Web que pode ser vista no navegador, ela contém os principais Insights da análise, uma tabela contendo quais casas comprar, por qual preço vende-las se elas forem reformadas ou não, além do possível lucro. Além disso também há dois mapas mostrando onde as casas se localizam e o preço médio das casas por região (ZipCode).

---
### Projeto Flask (flask_project):

> É uma aplicação que adiciona, edita e deleta uma lista de tarefas pelo mini-framework Flask, em Python, juntamente com um Banco de Dados gerenciado pelo PostgreSQL. Na interface web nós podemos manipular o Banco de Dados para adiconar tarefas, altera-las e remove-las. É uma aplicação simples, em que o foco não é a aplicação web, mas sim entender conceitos de API, como rotas, portas, verbos e códigos HTTP, entre outros, assim como criar um Banco de Dados para uma aplicação.

---
### Atualização diária de dados do Covid no Brazil e nos seus estados (covid_daily_update):

> Dentro dessa aplicação, há um contêiner com serviços do Airflow, Postgres e Redis, também há um script que cria um Banco de dados e duas tabelas se não existirem, a tabela "covid_brazil" contém dados gerais e diários do Covid no Brazil, e a tabela "covid_states" contém dados diários do Covid nos estados brasileiros. Além há um script que faz várias requisições em uma API para adicionar dados diários dentro das tabelas desde a primeira vez que se tornaram disponíveis até a data anterior a execução do script. Por fim há uma DAG que diariamente adiciona dados diariamente do Covid dentro das tabelas todo dia as 13h01.

---