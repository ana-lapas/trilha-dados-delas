# 🌸 Trilha Dados Delas

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![UFMS](https://img.shields.io/badge/UFMS-Projeto%20de%20Extens%C3%A3o-blue)](https://ufms.br/)
[![Developer Girls](https://img.shields.io/badge/Comunidade-Developer%20Girls-pink)](https://developer.girls/)

## 📖 Sobre o Projeto

O **Trilha Dados Delas** é um Produto Mínimo Viável (MVP) de software baseado em dados, desenvolvido como parte do **Projeto Integrador de Ciência dos Dados II** (Programa de Extensão UFMS Digital - 2026.2). 

O objetivo do projeto é reduzir a dispersão de informação e apoiar o primeiro contato de mulheres iniciantes ou em transição de carreira com a área de Tecnologia e Dados. A aplicação foi criada especialmente para a comunidade **Developer Girls**, oferecendo uma curadoria de recursos gratuitos, organizados e verificados.

O software transcende o formato de um PDF estático ao oferecer uma interface web interativa, com análise exploratória de dados e formulário de feedback integrado.

## ✨ Funcionalidades

O aplicativo foi dividido em abas para facilitar a navegação e a experiência da usuária:

*   **🎯 Curadoria de Cursos**: Lista interativa de cursos gratuitos (FGV, Data Science Academy, Santander, Cisco) com filtros por objetivo (Conceitos, Prática, Carreira). Inclui um "Diário de Bordo" (checklist) para acompanhamento do progresso.
*   **🎓 UFMS: Ciência de Dados**: Divulgação do curso superior de Tecnólogo em Ciência dos Dados (EaD e gratuito) oferecido pela UFMS. Apresenta dados oficiais do MEC, destaques da grade curricular (IA, Redes Neurais, Mineração de Dados) e informações sobre o vestibular anual gratuito.
*   **🤔 Não é a sua praia?**: Uma aba acolhedora que lista os outros 12 cursos de graduação EaD gratuitos oferecidos pela UFMS, mostrando alternativas de carreira para quem está indecisa.
*   **💌 Deixe seu Feedback**: Formulário integrado ao Formspree para envio de sugestões, dúvidas e avaliação da trilha (nota de 0 a 10) diretamente para a equipe responsável.
*   **📊 Análise de Dados**: Métricas em tempo real (KPIs) e gráficos de barra gerados dinamicamente a partir da base de dados de curadoria.

## 🛠️ Tecnologias Utilizadas

*   **Python**: Linguagem base do projeto.
*   **Streamlit**: Framework para criação da interface web interativa e componentes de UI.
*   **Pandas**: Biblioteca para estruturação e manipulação da base de dados (DataFrame).
*   **Requests**: Biblioteca para realizar a requisição HTTP (POST) do formulário de feedback para a API do Formspree.
*   **CSS Customizado**: Injeção de estilos para garantir uma identidade visual amigável, feminina e acessível.

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o projeto no seu computador.

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/trilha-dados-delas.git
cd trilha-dados-delas
```
### 2. Criar e Ativar um Ambiente Virtual (Venv)
#### No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### No Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
```bash
streamlit run app.py
```

O Streamlit abrirá automaticamente uma janela no seu navegador (geralmente no endereço http://localhost:8501).

### ☁️ Deploy na Nuvem
O projeto está configurado para ser publicado gratuitamente no Streamlit Community Cloud. Para fazer o deploy:

Faça o upload deste repositório (com os arquivos app.py e requirements.txt) no GitHub.

Acesse share.streamlit.io, conecte sua conta do GitHub e clique em "New app".

Selecione o repositório, a branch main e o arquivo app.py. Clique em "Deploy".

### 👩‍💻 Autoria e Contato
Desenvolvedora: Ana Paula Lapas Leão

Curso: Ciências de Dados (UFMS Digital)

Disciplina: Projeto Integrador de Ciência dos Dados II - T01-2026-2

Comunidade: Developer Girls

### 📅 Informações de Versão
Data de Publicação: 05/11/2026

Última Atualização: 05/11/2026

### Feito com 💜 e dedicação para incentivar a representatividade feminina na Ciência de Dados!