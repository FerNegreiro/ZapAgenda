# 🚀 ZapAgenda

O **ZapAgenda** é uma solução Full-stack robusta e inteligente desenvolvida para automação de agendamentos e envio de mensagens via WhatsApp. O sistema permite que utilizadores agendem lembretes personalizados através de uma interface web moderna, que são posteriormente processados por um motor de execução temporal (Worker) e enviados utilizando a **Evolution API**.

---

## 🛠️ Tecnologias Utilizadas

### Frontend
* **React + Vite**: Interface rápida, reativa e optimizada para performance.
* **Axios**: Gestão de pedidos HTTP para comunicação com a API.

### Backend
* **FastAPI (Python)**: Framework de alta performance com tipagem e documentação automática (Swagger/OpenAPI).
* **SQLAlchemy**: ORM para abstração e persistência de dados de forma segura.
* **SQLite**: Base de dados relacional leve para armazenamento local dos agendamentos.

### Integração e Automação
* **Evolution API**: Gateway profissional para integração com instâncias do WhatsApp.
* **Worker Pattern**: Serviço de monitorização em segundo plano que verifica o banco de dados a cada 30 segundos para garantir a entrega pontual das mensagens.

---

## 🏗️ Arquitetura do Projeto

O ecossistema é composto por três camadas principais que trabalham de forma síncrona:

| Componente | Função Principal |
| :--- | :--- |
| **API (FastAPI)** | Recebe os pedidos do site, valida os dados e guarda-os na base de dados. |
| **Vigilante (Worker)** | Um serviço independente que monitoriza o relógio e os agendamentos pendentes. |
| **Painel Web (React)** | Interface intuitiva onde o utilizador define o número, a mensagem e o horário. |

---

## 🚀 Como Executar

### 1. Backend & Worker
```bash
# Entrar na pasta do backend
cd backend

# Iniciar a API
python -m uvicorn app.main:app --reload

# Iniciar o Vigilante (num novo terminal)
python -m app.worker
2. Frontend
Bash
# Entrar na pasta do frontend
cd frontend

# Instalar dependências
npm install

# Iniciar o servidor de desenvolvimento
npm run dev
O sistema estará disponível em: http://localhost:5173

👤 Autor
Fernando Ivo Negreiro da Silva Full-stack Developer especializado em automação e arquitetura de software.Perfeito, agora vai **realmente em um único bloco só**, sem quebrar:

# 🚀 ZapAgenda

O **ZapAgenda** é uma solução full-stack robusta e inteligente desenvolvida para automação de agendamentos e envio de mensagens via WhatsApp. O sistema permite que usuários agendem lembretes personalizados através de uma interface web moderna, que são posteriormente processados por um motor de execução temporal (Worker) e enviados utilizando a **Evolution API**.

---

## 🛠️ Tecnologias Utilizadas

### 🎨 Frontend

* **React + Vite** → Interface rápida, reativa e otimizada para performance
* **Axios** → Gerenciamento de requisições HTTP

### ⚙️ Backend

* **FastAPI (Python)** → Alta performance com tipagem e documentação automática (Swagger/OpenAPI)
* **SQLAlchemy** → ORM para manipulação segura do banco de dados
* **SQLite** → Banco de dados relacional leve

### 🔗 Integração e Automação

* **Evolution API** → Integração com WhatsApp
* **Worker Pattern** → Serviço em segundo plano que verifica agendamentos a cada 30 segundos

---

## 🏗️ Arquitetura do Projeto

O sistema é dividido em três camadas principais:

| Componente             | Função                                      |
| ---------------------- | ------------------------------------------- |
| **API (FastAPI)**      | Recebe requisições, valida e salva os dados |
| **Worker (Vigilante)** | Monitora horários e dispara mensagens       |
| **Frontend (React)**   | Interface para criação dos agendamentos     |

---

## 🚀 Como Executar

### 🔧 Backend + Worker

```bash
cd backend
python -m uvicorn app.main:app --reload
python -m app.worker
```

### 💻 Frontend

```bash
cd frontend
npm install
npm run dev
```

🔗 Acesse: [http://localhost:5173](http://localhost:5173)

---

## 👤 Autor

**Fernando Ivo Negreiro da Silva**
Full-stack Developer focado em automação, integrações e arquitetura de software.
