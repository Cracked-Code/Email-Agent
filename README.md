# Email Agent 🤖

A full-stack autonomous AI email assistant built with LangGraph, FastAPI, and Next.js. Users connect their Gmail account via OAuth, search their inbox using natural language, and let the AI draft replies — with a human approval loop before anything is sent.

## Live Demo

[Link coming soon]

## How It Works

1. User connects their Gmail account via Google OAuth
2. The agent fetches and parses their inbox
3. User describes the email they're looking for in natural language
4. Gemini LLM finds the top 3 matches
5. User picks one
6. LLM drafts a reply on their behalf
7. User approves or rejects with feedback — agent rewrites if rejected
8. Approved email is sent via Gmail API

## Tech Stack

**Backend**
- **FastAPI** — REST API server
- **LangGraph** — agent orchestration and stateful graph execution
- **Google Gemini 2.5 Flash Lite** — language model via LangChain
- **Gmail API** — email fetching, OAuth 2.0 authentication
- **SQLAlchemy + PostgreSQL** — token storage per user
- **Python 3.13**

**Frontend**
- **Next.js 15** — React framework
- **Tailwind CSS** — styling

## Architecture

```
Next.js (frontend)
    ↓
FastAPI (backend)
    ↓
LangGraph agent
    ↓
Gmail API + Gemini
    ↓
PostgreSQL (token storage)
```

## Agent Graph

```
START
  ↓
fetch_emails
  ↓
select_email (LLM search)
  ↓
draft_reply
  ↓
approval ──── approved ──→ send email ──→ END
  ↑                         
  └──── rejected (with feedback) ──→ draft_reply
```

## Project Structure

```
email_agent/
├── server.py               # FastAPI entry point
├── main.py                 # CLI entry point
├── state.py                # EmailWriter TypedDict
├── graph.py                # LangGraph graph definition
├── database.py             # SQLAlchemy models and DB setup
├── config.py               # Environment variable loading
├── nodes/
│   ├── fetch_emails.py     # Fetches and parses Gmail messages
│   ├── select_email.py     # LLM-powered natural language search
│   ├── think.py            # LLM reasons about selected email
│   ├── draft_reply.py      # LLM drafts reply with feedback loop
│   └── approve.py          # Sends approved email via Gmail API
├── tools/
│   └── gmail.py            # Gmail OAuth service (loads from DB)
├── api/
│   └── routes/
│       ├── emails.py       # Email endpoints
│       └── auth.py         # OAuth login/callback endpoints
└── email-agent-ui/         # Next.js frontend
    └── app/
        └── page.js         # Single-page React UI
```

## Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/Cracked-Code/Email-Agent.git
cd Email-Agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Python dependencies

```bash
pip install fastapi uvicorn langgraph langchain-google-genai google-auth google-auth-oauthlib google-api-python-client python-dotenv sqlalchemy psycopg2-binary itsdangerous requests
```

### 4. Set up Google Cloud credentials

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project and enable the **Gmail API**
3. Create **OAuth 2.0 credentials** — type: **Web application**
4. Add `http://localhost:8000/auth/callback` as an authorized redirect URI
5. Download the JSON and save as `credentials.json` in the project root

### 5. Set up environment variables

Create a `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///./email_agent.db
```

### 6. Run the backend

```bash
uvicorn server:app --reload
```

### 7. Run the frontend

```bash
cd email-agent-ui
npm install
npm run dev
```

### 8. Connect your Gmail

Visit `http://localhost:3000`, enter your account name and display name, click **Connect To Gmail**, and complete the OAuth flow.

## Key Concepts

**State** — a `TypedDict` passed through every node, acting as shared memory for the agent during a task.

**Nodes** — individual units of work. Each reads from state and writes updates back.

**Conditional Edges** — routing logic between nodes. The approval node uses a conditional edge to either end the graph or loop back to redraft with feedback.

**Human-in-the-loop** — the agent pauses before sending, requiring explicit approval and capturing feedback to improve rewrites.

**OAuth 2.0** — users authenticate with Google once, token is stored in the database, and refreshed automatically on subsequent requests.

## Author

Nicholas Chopliani
[GitHub](https://github.com/Cracked-Code)
