# Santander 2025 - Back-End com Python

Este repositório contém os principais conceitos, práticas e projetos desenvolvidos durante o curso **Santander 2025 - Back-End com Python**.  
O foco do curso foi a construção de aplicações back-end modernas utilizando **Python**, **FastAPI**, **Banco de Dados**, **APIs RESTful** e boas práticas de desenvolvimento.

---

## 📚 Conteúdos aprendidos

### 🔹 Fundamentos de Bancos de Dados
- Linguagem **SQL** como padrão para interação com bancos relacionais.
- Diferença entre usar `SELECT *` e selecionar colunas específicas.
- Operações CRUD (Create, Read, Update, Delete).
- Métodos da **Python DB API** como `execute()` e `commit()`.

### 🔹 APIs RESTful
- Conceito de API: **Interface de Programação de Aplicações**.
- Convenções RESTful:
  - Recursos identificados por **URLs**.
  - Uso de verbos HTTP:
    - `GET` → consultar recursos.
    - `POST` → criar recursos.
    - `PUT`/`PATCH` → atualizar recursos.
    - `DELETE` → remover recursos.
- Diferença entre **Internet** (rede global de computadores) e **Web** (sistema de informações sobre a Internet).
- Tipos de APIs: **RESTful, SOAP, GraphQL**.

### 🔹 Desenvolvimento Web
- Diferença entre **Front-End** (HTML, CSS, JavaScript) e **Back-End** (servidores, banco de dados e lógica da aplicação).
- Função do **desenvolvedor fullstack**: atuar em front-end e back-end.
- O que é o **protocolo HTTP** e sua importância para a comunicação web.

### 🔹 FastAPI
- Criação de APIs assíncronas modernas e performáticas com **FastAPI**.
- Rotas para CRUD de recursos.
- Documentação automática da API com **Swagger UI** e **ReDoc**.

### 🔹 Testes com TDD (Test-Driven Development)
- Conceito de **TDD**: escrever testes antes da implementação.
- Testes unitários e de integração com **Pytest**.
- Uso do **httpx.AsyncClient** para testar rotas da API.
- Exemplo de API com FastAPI + MongoDB utilizando TDD.

---

## 🚀 Projetos desenvolvidos

### 1️⃣ API de Academia para Crossfit
- Construída com **FastAPI**.
- Estrutura assíncrona para lidar com múltiplas requisições.
- Operações CRUD para gerenciar alunos e treinos.

### 2️⃣ API com TDD e MongoDB
- Integração com banco **MongoDB**.
- Implementação de rotas para CRUD de usuários.
- Testes unitários e de integração com **Pytest**.
- Boas práticas de documentação de projeto.

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **FastAPI**
- **MongoDB**
- **SQL**
- **Pytest**
- **HTTPX**
- **Uvicorn**

---

## 📌 Como rodar os projetos

### Instalar dependências:
```bash
pip install fastapi uvicorn pymongo pytest httpx
