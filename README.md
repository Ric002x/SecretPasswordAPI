# SecretPasswordAPI

![Python](https://img.shields.io/badge/Python-v3.10.x-blue?style=flat-square&logo=python&logoColor=%23fff&labelColor=%232A3335&color=%230A5EB0) 
![Static Badge](https://img.shields.io/badge/FastAPI-v0.115.5-blue?style=flat-square&logo=fastapi&logoColor=%23fff&labelColor=%232A3335&color=%230A5EB0) 
![Licence](https://img.shields.io/badge/Licence-MIT-blue?style=flat-square&logoColor=%23fff&labelColor=%232A3335&color=%230A5EB0)

### Tabela de Conteúdos

1. [Sobre](#sobre)
2. [Tecnologias](#tecnologias)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Licença](#licença)

## 📋Sobre

Este projeto é uma API desenvolvida em Python, e inspirada no jogo [Wordle](https://www.nytimes.com/games/wordle/index.html), assim como o [Termo](https://term.ooo), sua versão brasileira. A ideia é simples: o jogador tenta adivinhar uma palavra secreta, e a API gerencia toda a lógica de validação e feedback.

A aplicação foi desenvolvida utilizando o framework [FastAPI](https://fastapi.tiangolo.com), conhecido por sua alta performance e facilidade na criação de APIs com Python.

---

## 🖥Tecnologias

- Python v3.10.x
- FastAPI v0.115.5

---

## 🔧Instalação

> Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

1. Crie um diretório para o projeto:
> Escolha um local em sua máquina e crie um diretório para armazenar os arquivos do projeto:

```bash
mkdir nome_do_diretorio
cd nome_do_diretorio
```

2. Clone o repositório no diretório criado:
> Baixe os arquivos do repositório para o diretório

```
git clone git@github.com:Ric002x/SecretPasswordAPI.git .
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
> O uso de um ambiente virtual ajuda a isolar as dependências do projeto. Para criar e ativar:

```
python.exe -m venv venv
```

Ative o ambiente virtual:

- Windows:
  ```bash
  .\venv\Scripts\activate
  ```

- Linux/Mac:
  ```bash
  source venv/bin/activate  
  ```

4. Instale as dependências do projeto:
> Com o ambiente virtual ativado (se estiver usando), instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

Pronto! Após essas etapas, o projeto estará configurado e pronto para ser inicializado.


### 🚀Inicializando o projeto

Para rodar o servidor de desenvolvimento e testar a API, utilize o seguinte comando:

```
python run.py
```

A aplicação estará rodando em http://127.0.0.1:8000 ou http://localhost:8000

Verifique a documentação simplificada em http://localhost:8000/docs

---

## 📝Uso

> Explicação das funcionalidades da aplicação, assim como seus endpoints

### ⌛Schedule

A aplicação conta com um sistema automático de seleção de palavras, desenvolvido sem o uso de bibliotecas externas, funcionando de forma independente da API.

O schedule foi projetado para que, diariamente, às 12 horas, uma nova palavra seja escolhida e adicionada ao banco de dados. Esse banco é essencial para evitar repetições, garantindo que nenhuma palavra seja reutilizada dentro de um período mínimo de 50 dias.

Caso a palavra selecionada já esteja presente no banco, o sistema tentará escolher outra, repetindo esse processo até encontrar uma palavra inédita. Quando uma nova palavra é salva, e o banco atinge o limite de 51 registros, a palavra mais antiga é removida automaticamente. Isso evita o acúmulo excessivo de dados na tabela, mantendo-a sempre atualizada e otimizada.

### 🔗Endpoints:

#### GET /current-word
- **Descrição**: Retorna a última palavra gerada pelo schedule
- **Exemplo de Resposta**:
```json
{
  "word": "palavra"
}
```
- **Status**:
  - 200: OK

---

#### GET /validate/{word}
> Substitua `word`, pela palavra que deseja validar
- **Descrição**: Verifica se a palavra enviada na URL é valida e existente
- **Exemplo de Resposta**:
```json
{
  "validate": true
}
```

Ou

```json
{
  "validate": false
}
```
- **Status**:
  - 200: OK

---

#### GET /check-word/{word}
> Substitua `word`, pela palavra que deseja validar
- **Descrição**: Compara a palavra do dia com a palavra enviada na URL, e retorna um feedback verificando os acertos e erros
- **Exemplos de Resposta**:
```json
{
  "status": "incorreto",
  "validation": [0, 1, 2, 0, 1]
}
```

OU

```json
{
  "status": "correto",
  "validation": [2, 2, 2, 2, 2]
}
```
- Detalhes do campo `validation`:
  - A chave `validation` retorna uma lista numérica que valida cada letra da palavra enviada:
    - 0: A letra não está presente na palavra do dia.
    - 1: A letra existe, mas está na posição errada.
    - 2: A letra existe e está na posição correta.

---

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).

