# 🚀 Mini-Projeto Integrado em Python (FastAPI, Pandas e FP)

**Aluno:** Marllyson Farias
**Matrícula:** 2025 0513 5972
**Disciplina:** Linguagem Python
**Professor:** Raphael Mauricio Sanches de Jesus

Este projeto implementa uma aplicação enxuta que integra Pandas para processamento de dados, Programação Funcional (FP) para um desafio lógico e FastAPI para exposição dos resultados via API.

## 🧱 Estrutura do Projeto
seu_projeto/ ├── data/ │ └── dados.csv # Dados brutos ├── src/ │ ├── core/ │ │ └── metrics.py # Desafio FP (analisar) │ ├── app.py # FastAPI endpoints (/health, /stats, /soma) │ └── make_stats.py # Script Pandas (gera stats.json) ├── stats.json # Estatísticas geradas ├── requirements.txt # Dependências └── README.md

## 🛠️ Como Instalar e Executar

Execute todos os comandos a partir da raiz do projeto, utilizando o Terminal Integrado do PyCharm (que garante o uso correto do ambiente virtual).

### 1. Instalação das Dependências

Instale as bibliotecas necessárias usando o `requirements.txt`:

```bash
pip install -r requirements.txt

Você atingiu a etapa final! O envio do projeto é feito através de um Repositório Git (GitHub ou GitLab), que é a forma padrão e profissional de compartilhar código.

Se você já tiver uma conta e o Git instalado em sua máquina, siga os passos abaixo para enviar todos os arquivos.

📝 Guia de Envio para GitHub/GitLab

Passo 0: Finalizar o README.md (Crucial)

Antes de enviar, crie o arquivo README.md na raiz do seu projeto. Use as instruções que funcionaram para você.

Modelo Sugerido para README.md:
Markdown

# 🚀 Mini-Projeto Integrado em Python (FastAPI, Pandas e FP)

**Aluno:** Marcelo
**Disciplina:** Linguagem Python
**Professor:** Raphael Mauricio Sanches de Jesus

Este projeto implementa uma aplicação enxuta que integra Pandas para processamento de dados, Programação Funcional (FP) para um desafio lógico e FastAPI para exposição dos resultados via API.

## 🧱 Estrutura do Projeto

seu_projeto/ ├── data/ │ └── dados.csv # Dados brutos ├── src/ │ ├── core/ │ │ └── metrics.py # Desafio FP (analisar) │ ├── app.py # FastAPI endpoints (/health, /stats, /soma) │ └── make_stats.py # Script Pandas (gera stats.json) ├── stats.json # Estatísticas geradas ├── requirements.txt # Dependências └── README.md


## 🛠️ Como Instalar e Executar

Execute todos os comandos a partir da raiz do projeto, utilizando o Terminal Integrado do PyCharm (que garante o uso correto do ambiente virtual).

### 1. Instalação das Dependências

Instale as bibliotecas necessárias usando o `requirements.txt`:

```bash
pip install -r requirements.txt

2. Geração do stats.json (Pandas e FP)

Este passo processa o data/dados.csv, calcula as estatísticas simples (Pandas) e executa o mini-desafio FP, salvando o resultado final em stats.json.
Bash

python src/make_stats.py

(Verifique se o stats.json aparece na raiz após este comando.)

3. Como Subir a API (FastAPI)

Inicie o servidor Uvicorn para expor os endpoints.
Bash

uvicorn src.app:app --reload

A API estará acessível em http://127.0.0.1:8000.