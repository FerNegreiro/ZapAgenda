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

🔗 Acesse: http://localhost:5173

---

## 👤 Autor

**Fernando Ivo Negreiro da Silva**
Full-stack Developer focado em automação, integrações e arquitetura de software.
