# 🚨 Incident Response Agent

An AI-powered incident management and memory system designed to help engineering teams **record, investigate, resolve, and learn from production incidents**.

The system maintains a memory of previous incidents, including symptoms, root causes, resolutions, and operational knowledge, so engineers can use historical incidents to respond to future problems more efficiently.

---

## ✨ Features

* 📝 **Incident Management**

  * Create and track production incidents
  * Store incident descriptions, services, severity, and status
  * Track open and resolved incidents

* 🧠 **Incident Memory**

  * Store previous incidents and their resolutions
  * Preserve root-cause information
  * Use historical incidents as operational knowledge

* 🤖 **AI-Assisted Response**

  * Analyze incident information using Google's Generative AI
  * Provide context based on previous incidents
  * Assist engineers during incident investigation

* 🗄️ **PostgreSQL Database**

  * Persistent incident storage
  * SQLAlchemy-based database layer

* ⚡ **FastAPI Backend**

  * REST API for incident operations
  * Automatic API documentation
  * Modular backend architecture

* 💻 **React Frontend**

  * Modern incident operations dashboard
  * Incident overview and status information
  * Recent incident memory

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      React UI        │
                    │      Vite            │
                    └──────────┬───────────┘
                               │
                               │ REST API
                               ▼
                    ┌──────────────────────┐
                    │     FastAPI API      │
                    │      Backend         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌──────────────┐  ┌─────────────┐
       │ PostgreSQL  │  │  SQLAlchemy  │  │ Google GenAI│
       │  Database   │  │     ORM      │  │     AI      │
       └─────────────┘  └──────────────┘  └─────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL
* Psycopg

### AI

* Google Generative AI / Gemini

### Development

* Git
* GitHub
* Python Virtual Environment
* npm

---

## 📁 Project Structure

```text
incident-response-agent/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── incidents.py
│   │   │
│   │   ├── database/
│   │   │   └── connection.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/Charanrakesh/incident-response-agent.git
cd incident-response-agent
```

---

## 2. Backend Setup

Create a Python virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
cd backend
python -m pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the backend directory.

Example:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/incident_db

GOOGLE_API_KEY=your_google_api_key
```

### ⚠️ Security

Never commit `.env` files, API keys, passwords, database credentials, or tokens to GitHub.

Make sure `.env` is included in `.gitignore`.

---

## 4. Start PostgreSQL

Make sure PostgreSQL is installed and running.

Create the database configured in your `DATABASE_URL`.

For example:

```text
incident_db
```

The application uses SQLAlchemy to communicate with PostgreSQL.

---

## 5. Start the Backend

From the `backend` directory:

```powershell
python -m uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 🎨 Frontend Setup

Open a **new terminal**.

Go to the frontend:

```powershell
cd incident-response-agent\frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🔄 Running the Complete Application

You need two terminals.

### Terminal 1 — Backend

```powershell
cd incident-response-agent
.\.venv\Scripts\Activate.ps1
cd backend
python -m uvicorn app.main:app --reload
```

### Terminal 2 — Frontend

```powershell
cd incident-response-agent\frontend
npm run dev
```

Then open the frontend URL shown by Vite.

---

# 📡 API

The backend exposes REST endpoints for incident management.

The complete API can be explored through FastAPI Swagger:

```text
http://127.0.0.1:8000/docs
```

Typical operations include:

```text
POST    /incidents
GET     /incidents
GET     /incidents/{id}
PUT     /incidents/{id}
DELETE  /incidents/{id}
```

> The exact available endpoints depend on the current implementation in the backend.

---

# 🧠 How the Incident Memory Works

The system is designed around the idea that **previous incidents contain valuable operational knowledge**.

A typical workflow is:

```text
New Incident
     │
     ▼
Incident Details
     │
     ▼
Search Historical Incidents
     │
     ▼
Identify Similar Problems
     │
     ▼
AI-Assisted Analysis
     │
     ▼
Root Cause
     │
     ▼
Resolution
     │
     ▼
Store Incident Memory
```

Over time, the incident database becomes a knowledge base containing information about previous production problems.

---

# 📊 Incident Lifecycle

An incident can move through states such as:

```text
OPEN
  │
  ▼
INVESTIGATING
  │
  ▼
RESOLVED
```

The system can use information from resolved incidents to assist with future incidents.

---

# 🔐 Environment & Security

Sensitive information should be stored using environment variables.

Never commit:

```text
.env
*.env
API keys
database passwords
GitHub tokens
credentials
```

The repository's `.gitignore` should exclude these files.

---

# 🧪 Development

Backend:

```powershell
cd backend
python -m uvicorn app.main:app --reload
```

Frontend:

```powershell
cd frontend
npm run dev
```

---

# 📌 Current Status

The project is currently under active development.

### Implemented

* [x] FastAPI backend
* [x] PostgreSQL database integration
* [x] SQLAlchemy database layer
* [x] Incident API
* [x] React/Vite frontend
* [x] Incident dashboard
* [x] Google Generative AI integration
* [x] Basic incident memory functionality

### Planned Improvements

* [ ] Advanced incident similarity search
* [ ] Better AI-generated root-cause analysis
* [ ] Automated runbook recommendations
* [ ] Authentication and authorization
* [ ] Incident timeline
* [ ] Advanced analytics
* [ ] Production deployment
* [ ] Automated testing
* [ ] CI/CD pipeline
* [ ] Observability and monitoring

---

# 🎯 Project Goal

The goal of the Incident Response Agent is to transform incident handling from a purely reactive process into a **memory-driven engineering workflow**.

Instead of engineers repeatedly solving the same classes of problems from scratch, the system aims to preserve organizational knowledge and make previous incident experience available when it matters.

---

# 👨‍💻 Author

**Charanrakesh**

GitHub:

https://github.com/Charanrakesh

---

## 📄 License

This project is currently intended as a development and learning project.

A formal open-source license can be added when the project is ready for public distribution.
<img width="1366" height="768" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/f0c4d41a-cbe7-4eea-be9c-d9850bb55861" />
<img width="1366" height="768" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/a29f10e0-7085-422b-8a2e-38f7878651df" />
<img width="1366" height="768" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/fba2562f-78d4-4923-813f-43dc789c4681" />
