# Agente de Cobrança com LangChain

Este projeto implementa um agente de cobrança inteligente, capaz de interagir com usuários via chat, consultar um banco de dados de dívidas e devedores, e gerar acordos de pagamento personalizados. Utiliza LangChain, OpenAI e uma interface web em Streamlit.

## Descrição do Projeto

O "Agente de Cobrança" é um assistente virtual que automatiza o processo de negociação de dívidas. Ele:
- Solicita o CPF do cliente
- Consulta dívidas e acordos ativos no banco de dados
- Propõe acordos personalizados
- Registra novos acordos conforme a negociação
- Mantém o contexto da conversa para negociações mais naturais

## Funcionalidades

- **Chat interativo:** Interface web via Streamlit para interação com o agente.
- **Memória de conversa:** O agente mantém o contexto das conversas.
- **Consulta de CPF:** Busca dados do devedor pelo CPF.
- **Consulta de dívidas:** Mostra o valor total das dívidas pendentes.
- **Verificação de acordos:** Informa se já existe acordo ativo e seu valor.
- **Registro de acordo:** Permite registrar um novo acordo, com valor e número de parcelas.


## Tecnologias Utilizadas

- LangChain
- Streamlit
- PostgreSQL

## Visão Geral do Banco de Dados

O banco de dados utilizado foi criado com PostgreSQL. O diagrama entidade-relacionamento (ER) pode ser visualizado abaixo:

![Diagrama ER](docs/ERD.png)

### Estrutura das Tabelas

O banco de dados contém as seguintes tabelas:
- `devedores`: informações sobre os devedores
- `dividas`: registros das dívidas
- `acordos`: acordos de pagamento gerados
- `negociadores`: responsáveis pelas negociações

A definição das tabelas está no arquivo [`create_db.sql`](db/create_db.sql), e exemplos de dados podem ser encontrados em [`insert_db.sql`](db/insert_db.sql).

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/stevillis/agente-cobranca-langchain.git
   cd agente-cobranca-langchain
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure o banco de dados:**
   - Crie um banco PostgreSQL e execute os scripts em `db/create_db.sql` e `db/insert_db.sql`.
4. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto com as variáveis:
     ```env
     DB_HOST=localhost
     DB_PORT=5432
     DB_NAME=nome_do_banco
     DB_USER=usuario
     DB_PASSWORD=senha
     OPENAI_API_KEY=sua_chave_openai
     ```
5. **Execute a aplicação:**
   ```bash
   streamlit run src/app.py
   ```
6. **Acesse a interface web:**
   - Abra o navegador em `http://localhost:8501`

## Requisitos

- Python 3.11+
- PostgreSQL
- Chave de API OpenAI

## Referência

Este projeto segue o artigo: [Introdução à criação de AI Agents com LangChain : Criando um Agente de Cobrança](https://www.dio.me/articles/introducao-a-criacao-de-ai-agents-com-langchain-criando-um-agente-de-cobranca-f1139653ff1b)
