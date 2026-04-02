#  API de Pokémons com FastAPI

Uma API simples desenvolvida com FastAPI que realiza operações de CRUD (Create, Read, Update, Delete) sobre uma lista de Pokémons.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn

---

## Funcionalidades

A API permite:

- Criar um novo Pokémon
- Listar todos os Pokémons
- Atualizar um Pokémon existente
- Deletar um Pokémon

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie o ambiente virtual

```bash
python3 -m venv venv
```

### 3. Ative o ambiente

Linux/Mac:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install fastapi uvicorn
```

### 5. Rode a aplicação

```bash
uvicorn main:app --reload
```

---

##  Como testar a API

Acesse no navegador:

```
http://127.0.0.1:8000/docs
```

Essa interface permite testar todas as rotas da API.

---

## Rotas disponíveis

### Listar Pokémons
```
GET /pokemons
```

---

###  Criar Pokémon
```
POST /pokemons
```

Exemplo de JSON:

```json
{
  "name": "Pikachu",
  "type": "Electric"
}
```

---

### Atualizar Pokémon
```
PUT /pokemons/{pokemon_id}
```

---

### Deletar Pokémon
```
DELETE /pokemons/{pokemon_nome}
```

---

## Observação

Os dados são armazenados em memória (lista Python), ou seja:

> Ao reiniciar o servidor, todos os dados serão perdidos.

---

## Objetivo

Projeto desenvolvido para prática de conceitos de API REST e operações CRUD.

---

##  Autor

João Vitor


