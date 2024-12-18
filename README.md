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

Este projeto é inspirado no jogo [Wordle](https://www.nytimes.com/games/wordle/index.html), assim como o [Termo](https://term.ooo), sua versão brasileira. Ele é composto por um backend desenvolvido com [FastAPI](https://fastapi.tiangolo.com), um frontend simples baseado em templates, e uma configuração [Docker](https://www.docker.com) otimizada que garante uma boa integração entre os dois.

O jogador tenta adivinhar uma palavra secreta, e o sistema gerencia toda a validação e o feedback, garantindo uma experiência dinâmica e fluida.

O [FastAPI](https://fastapi.tiangolo.com), reconhecido por sua alta performance e simplicidade, fornece as ferramentas necessárias para que o frontend complemente a aplicação, demonstrando o uso da API. Além disso, o setup Docker foi projetado para facilitar tanto o deploy quanto o ambiente de desenvolvimento.

---

## 🖥Tecnologias

- Python v3.10.x
- FastAPI v0.115.5
- Docker v27.2.0

---

## 🔧Instalação

> Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

Certifique-se de que o Docker está instalado e atualizado em sua máquina, pois ele é essencial para rodar a aplicação. Caso ainda não tenha o Docker, você pode fazer o download no site oficial: [Docker](https://www.docker.com).

Para verificar se o Docker está instalado e funcionando corretamente:

```
docker --version
docker run hello-world
```

### Passos para instalação

1. Crie um diretório para o projeto:
> Escolha um local em sua máquina e crie um diretório para armazenar os arquivos do projeto:

```bash
mkdir nome_do_diretorio
cd nome_do_diretorio
```

2. Clone o repositório no diretório criado e acesse-o:
> Baixe os arquivos do repositório para o diretório

```
git clone https://github.com/Ric002x/SecretPasswordAPI.git
cd /SecretPasswordAPI
```

3. Configure o arquivo `.env`:
> Configure as variáveis de ambiente necessárias

- No Windows:

  ```bash
  cd backend/
  copy .env-example .env
  notepad .env
  ```
- No Linux:

  ```bash
  cd backend/
  mv .env-example .env
  nano .env
  ```

Exemplo de conteúdo para o .env:

  ```env
  FASTAPI_CONFIG="development"
  DATABASE_URL="sqlite///my_database.db"
  DATABASE_URL_TESTS="sqlite///test.db"
  ```

4. Rode a aplicação com Docker:
> O projeto vem com uma configuração Docker pronta para uso. Para inicializar a aplicação, execute o seguinte comando:

```
docker compose --build -d
```

Isso compilará e iniciará os containers necessários.

A aplicação estará rodando em http://127.0.0.1 ou http://localhost

---

## 📝Uso

> Explicação das funcionalidades da aplicação, assim como seus endpoints

### ⌛Schedule

A aplicação conta com um sistema automático de seleção de palavras, desenvolvido sem o uso de bibliotecas externas, funcionando de forma independente da API.

O schedule foi projetado para que, diariamente, às 12 horas, uma nova palavra seja escolhida e adicionada ao banco de dados. Esse banco é essencial para evitar repetições, garantindo que nenhuma palavra seja reutilizada dentro de um período mínimo de 50 dias.

Caso a palavra selecionada já esteja presente no banco, o sistema tentará escolher outra, repetindo esse processo até encontrar uma palavra inédita. Quando uma nova palavra é salva, e o banco atinge o limite de 51 registros, a palavra mais antiga é removida automaticamente. Isso evita o acúmulo excessivo de dados na tabela, mantendo-a sempre atualizada e otimizada.

### 🔗Endpoints:

#### GET /api/current-word
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

#### GET /api/validate/{word}
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

#### GET /api/check-word/{word}
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

