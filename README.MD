# Sobre
Ester README tem por objetivo fornecer as informações necessárias para avaliação de candidatos para a linguagem Python.
#  🏗   O que fazer?

Você deve realizar um fork deste repositório e, ao finalizar, enviar o link do seu repositório para a nossa equipe. Lembre-se, NÃO é necessário criar um Pull Request para isso, nós iremos avaliar e retornar por email o resultado do seu teste.

# 🚨 Requisitos

- A API deverá ser construída em Python
- Implementar autenticação e deverá seguir o padrão **JWT**, lembrando que o token a ser recebido deverá ser no formato **Bearer**
- Recomendamos uso de Flask ou Django como framework, no  entanto outros frameworks serão aceitos.
- Para a comunicação com o banco de dados utilize algum **ORM**/**ODM**
- Bancos relacionais permitidos:
      - MySQL
      - MariaDB
      - Postgre
- Bancos não relacionais permitidos:
      - MongoDB
- Sua API deverá seguir os padrões Rest na construção das rotas e retornos
- Sua API deverá conter a collection/variáveis do postman ou algum endpoint da documentação em openapi para a realização do teste
- Descrever de forma clara em seu README os passos para executar seu projeto.
# 🕵🏻‍♂️ Itens a serem avaliados

- Estrutura do Projeto
- Segurança da API, como autenticação, senhas salvas no banco, SQL Injection e outros
- Boas práticas da Linguagem/Framework
- Seu projeto deverá seguir tudo o que foi exigido na seção [O que desenvolver?](##--o-que-desenvolver)
- Migrations para a criação das tabelas do banco relacional caso seja escolhido um banco relacional.

# 🎁 Extra

Esses itens não são obrigatórios, porém desejados.

- Testes unitários
- Linter
- Code Formater


# 🖥 O que desenvolver?
Você deverá construir uma API que faça jogos da mega sena, o usuario deverá escolher a quantidade de dezenas por jogo e sua API irá gerar aleatoriamente dezenas para o usuário. O usuário poderá consultar o resultado do ultimo jogo e comparar com suas dezenas para conferir quantos numeros acertou.

- IMPORTANTE: Para obter o ultimo resultado da megasena você deverá fazer um webscrapping no Google. A seguinte pesquisa te traz o que você precisa obter: https://www.google.com/search?q=caixa+mega+sena 


Rotas necessárias para API:

- Usuário

    - Cadastro
    - Login
    - Edição (o usuário deve está autenticado)
    - Exclusão lógica (O usuário so pode deletar a propria conta)


- Megasena (todos endpoints devem exigir autenticação)
    
    - Realizar um novo jogo.
        - Deverá receber quantos dezenas (entre 6 e 10) o usuário deseja e sortear dezenas de acordo com a quantidade escolhida.
    - Consultar o resultado da ultima megasena (O webscrapping citado acima).
    - Ver quantos numeros acertou no seu ultimo jogo.
    - Listar seus jogos passados.

# 🔗 Links

- Documentação JWT https://jwt.io/
- Frameworks:

    -   https://www.djangoproject.com
    -   https://flask.palletsprojects.com/en/1.1.x/

- Bibliotecas que podem te ajudar:
    - random
    - pandas
    - cfscrape
    - bs4
    - lxml

# Rotas
- para testar a aplicação é recomendado a utilização do insomnia basta instalar e importar o arquivo Insomnia_2021-04-15

## USER
## URI/user/create/
- POST
### BODY
```json
{
	"username":"kaiooliveira",
	"first_name":"Kaio Henrique",
	"last_name":"Oliveira da Silva",
	"email":"kaiohenrique2601@gmail.com",
	"password":"1234"
}
```
### Response
```json
{
  "id": 9,
  "username": "kaio26",
  "first_name": "Kaio Henrique",
  "last_name": "Oliveira da Silva",
  "email": "kaiohenrique2601@gmail.com"
}
```
## URI/user/
- DELETE
### BODY
```json
NO BODY
```
### Response
```json
204 NO CONTENT
```
## URI/login/
- POST
### BODY
```json
{
	"username":"kaio26",
	"password":"123456"
}
```
### Response
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxODYwMTQ5OCwianRpIjoiYzZkODBhODBjZDljNGExOGEyNWViYjA0NmJlZGJiMzUiLCJ1c2VyX2lkIjoyfQ.bBOPnR6wvkNSeaDn9Iznl8dolvC-x3ngO18_N3apLL0",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE4NTE1Mzk4LCJqdGkiOiIxNTU3MTI3MjRkMWY0YWM4YjY3ZGRmNDIzYWQ1M2JiNiIsInVzZXJfaWQiOjJ9.vi8JJJY8FVPquK6UvYoGUhrj5vC6PpVYYxV4BuY4Pt0"
} 
```
## URI/user/
- PATCH
### BODY
```json
{
	"email":"kaiohenrique2601@outlook.com"
}
```
### Response
```json
{
  "id": 9,
  "username": "kaio26",
  "first_name": "Kaio Henrique",
  "last_name": "Oliveira da Silva",
  "email": "kaiohenrique2601@outlook.com"
}
```
## GAMES
## URI/games/result/
- GET
### BODY
- No body
### Response
```json
{
  "concurso": "Concurso 2362 (14/04/21)",
  "numeros": [
    3,
    20,
    22,
    32,
    35,
    50
  ]
}
```
## URI/games/points/
- GET
### BODY
- No body
### Response
```json
{
  "points": 0,
  "game": {
    "id": 3,
    "numbers": "[9, 19, 24, 46, 54, 56]",
    "date": "2021-04-15",
    "user": {
      "id": 2,
      "username": "kaiosuper",
      "first_name": "",
      "last_name": "",
      "email": ""
    }
  },
  "concurse": "Concurso 2362 (14/04/21)",
  "result_numbers": [
    3,
    20,
    22,
    32,
    35,
    50
  ],
  "game_numbers": [
    9,
    19,
    24,
    46,
    54,
    56
  ]
}
```
## URI/games/
- GET
### BODY
- No body
### Response
```json
[
  {
    "id": 1,
    "numbers": "[14, 27, 35, 46, 58, 58]",
    "date": "2021-04-15",
    "user": {
      "id": 1,
      "username": "kaio",
      "first_name": "",
      "last_name": "",
      "email": "kaiohenrique2601@outlook.com"
    }
  },
  {
    "id": 2,
    "numbers": "[11, 14, 19, 41, 53, 55]",
    "date": "2021-04-15",
    "user": {
      "id": 1,
      "username": "kaio",
      "first_name": "",
      "last_name": "",
      "email": "kaiohenrique2601@outlook.com"
    }
  }
]
```
## URI/games/
- GET
### BODY
```json
{
	"tens":6
}
```

### Response
```json
{
  "id": 4,
  "numbers": "[6, 13, 30, 38, 40, 60]",
  "date": "2021-04-15",
  "user": {
    "id": 2,
    "username": "kaiosuper",
    "first_name": "",
    "last_name": "",
    "email": ""
  }
}
```
