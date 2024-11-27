# SecretPasswordAPI

![Python](https://img.shields.io/badge/Python-v3.12-blue?style=flat-square&logo=python&logoColor=%23fff&labelColor=%232A3335&color=%230A5EB0)
![Static Badge](https://img.shields.io/badge/FastAPI-v0.115.5-blue?style=flat-square&logo=fastapi&logoColor=%23fff&labelColor=%232A3335&color=%230A5EB0)
![Licence](https://img.shields.io/badge/Licence-MIT-blue?style=flat-square&logoColor=%23fff&labelColor=%232A3335&color=%230A5EB0)

Este projeto é uma API desenvolvida em Python, e inspirada no jogo [Wordle](https://www.nytimes.com/games/wordle/index.html), assim como o [Termo](https://term.ooo), sua versão brasileira. A ideia é simples: o jogador tenta adivinhar uma palavra secreta, e a API gerencia toda a lógica de validação e feedback.

A aplicação foi desenvolvida utilizando o framework [FastAPI](https://fastapi.tiangolo.com), conhecido por sua alta performance e facilidade na criação de APIs com Python.

---

## 🔧 Configurando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 🔧 Instalação

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

### 🚀 Inicializando o projeto

Para rodar o servidor de desenvolvimento e testar a API, utilize o seguinte comando:

```
python main.py
```

A aplicação estará rodando em http://127.0.0.1:8000 ou http://localhost:8000
