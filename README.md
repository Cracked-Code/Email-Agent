# Email Agent 🤖

A full-stack autonomous AI email assistant built with LangGraph, FastAPI, and Next.js. Users connect their Gmail account via OAuth, search their inbox using natural language, and let the AI draft replies — with a human approval loop before anything is sent.

## Live Demo

🔗 [https://email-agent-gold-ten.vercel.app](https://email-agent-gold-ten.vercel.app)

> **Note**: This app is currently live, however it is not verified via Google's OAuth, so it will show up with a warning ("Google hasn't verified this app") during login. Feel free to ignore that — it doesn't affect functionality. To run it with your own Gmail account on your local machine, follow the local setup instructions below and add your email as a test user in Google Cloud Console.

## How It Works

1. User connects their Gmail account via Google OAuth
2. The agent fetches and parses their inbox (excluding Promotions/Social categories by default)
3. User describes the email they're looking for in natural language
4. A lightweight keyword pre-filter narrows the inbox down to likely candidates before any LLM call is made
5. Gemini LLM ranks the filtered candidates and returns the best matches
6. If no relevant match is found, the agent automatically paginates further back into the inbox and retries, up to a capped number of attempts
7. User picks a match from the results
8. LLM drafts a reply on their behalf
9. User approves or rejects with feedback — agent rewrites if rejected
10. Approved email is sent via Gmail API

## Tech Stack

**Backend**
- **FastAPI** — REST API server
- **LangGraph** — agent orchestration and stateful graph execution
- **Google Gemini 2.5 Flash Lite** — language model via LangChain
- **Gmail API** — email fetching, OAuth 2.0 authentication, pagination
- **SQLAlchemy + PostgreSQL** — token storage per user (Supabase)
- **Python 3.13**

**Frontend**
- **Next.js 15** — React framework (App Router)
- **Tailwind CSS** — styling

**Infrastructure**
- **Render** — backend hosting
- **Vercel** — frontend hosting
- **Supabase** — managed PostgreSQL database

## Architecture

```
Next.js (Vercel)
    ↓
FastAPI (Render)
    ↓
LangGraph agent
    ↓
Gmail API + Gemini
    ↓
PostgreSQL (Supabase)
```

## Agent Graph

```
START
  ↓
fetch_emails
  ↓
select_email (keyword pre-filter → LLM search)
  ↓  (no match found)
  └──── fetch next page ──→ select_email (retry, up to N attempts)
  ↓  (match found)
draft_reply
  ↓
approval ──── approved ──→ send email ──→ END
  ↑
  └──── rejected (with feedback) ──→ draft_reply
```

## Search Design Notes

Early versions of the search pipeline sent full email bodies for a fixed batch of recent emails straight to the LLM, and forced it to always return a fixed number of "best" matches. This caused two problems: relevant but older emails outside the fetch window were invisible to search, and when nothing genuinely relevant existed, the LLM was forced to return irrelevant results anyway (e.g. promotional emails) rather than reporting no match.

The current design addresses both:
- **Pagination retry loop** — if the LLM finds nothing relevant in the current page of fetched emails, the backend automatically fetches the next page (using Gmail's `pageToken`) and retries, up to a capped number of attempts, so older emails are reachable without fetching the entire mailbox up front.
- **Keyword pre-filter** — before any LLM call, candidate emails are narrowed down via cheap local string matching against the query. Only pre-filtered candidates (with truncated body snippets, not full HTML) are sent to the LLM, significantly reducing token usage per search.
- **Explicit "no match" signal** — the LLM is instructed to return `"False"` when nothing is genuinely relevant, rather than being forced to always return a fixed count of results.

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
│   ├── fetch_emails.py     # Fetches and parses Gmail messages (paginated)
│   ├── select_email.py     # Keyword pre-filter + LLM-powered natural language search
│   ├── think.py            # LLM reasons about selected email
│   ├── draft_reply.py      # LLM drafts reply with feedback loop
│   └── approve.py          # Sends approved email via Gmail API
├── tools/
│   └── gmail.py            # Gmail OAuth service (loads token from DB)
├── api/
│   └── routes/
│       ├── emails.py       # Email endpoints, including search retry/pagination orchestration
│       ├── auth.py         # OAuth login/callback endpoints
│       └── health.py       # Health check endpoint (used for uptime pinging)
└── email-agent-ui/         # Next.js frontend
    └── app/
        ├── page.js         # Single-page React UI (multi-step flow)
        ├── privacy/
        │   └── page.js     # Privacy Policy page
        └── terms/
            └── page.js     # Terms of Service page
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

> **Note:** Virtual environments store an absolute path to the Python interpreter. If you move or rename the project folder after creating `venv`, you'll need to delete and recreate it — otherwise you may see errors like `Fatal error in launcher` when running `uvicorn`.

### 3. Install Python dependencies

```bash
pip install fastapi uvicorn langgraph langchain-google-genai google-auth google-auth-oauthlib google-api-python-client python-dotenv sqlalchemy psycopg2-binary itsdangerous requests
```

Or, if a `requirements.txt` is present:

```bash
pip install -r requirements.txt
```

### 4. Set up Google Cloud credentials

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project and enable the **Gmail API**
3. Create **OAuth 2.0 credentials** — type: **Web application**
4. Add `http://localhost:8000/auth/callback` as an authorized redirect URI
5. Download the JSON and save as `credentials.json` in the project root
6. Go to **OAuth consent screen** → **Test users** and add your Gmail address
7. Under **OAuth consent screen**, make sure the **App name**, **Home page URL**, **Privacy Policy URL**, and **Terms of Service URL** all match what's actually live on your deployed frontend — mismatches here will block verification.

> **Note on verification:** Google's OAuth verification requires your home page URL to be on a domain you can prove ownership of via Google Search Console (DNS verification). Shared platform subdomains (e.g. `*.vercel.app`, `*.pages.dev`, `*.onrender.com`) generally cannot be verified this way, since you don't control DNS for the shared parent domain. A custom domain pointed at your existing host (Vercel, etc.) is required for verification.

### 5. Set up environment variables

Create a `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///./email_agent.db
SECRET_KEY=your_secret_key_here
GOOGLE_CREDENTIALS={"web":{"client_id":"...","client_secret":"...","redirect_uris":["http://localhost:8000/auth/callback"],"auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token"}}
```

### 6. Run the backend

```bash
uvicorn server:app --reload --port 8000
```

### 7. Run the frontend

```bash
cd email-agent-ui
npm install
npm run dev
```

> **Note:** `npm run dev` only starts the Next.js frontend. The FastAPI backend must be run separately (see step 6) — they are two independent processes.

### 8. Connect your Gmail

Visit `http://localhost:3000`, enter your account name and display name, click **Connect To Gmail**, and complete the OAuth flow.

## Deployment Notes

- **Backend (Render free tier)** hibernates after ~15 minutes of inactivity. A `/health` endpoint is included and pinged periodically via UptimeRobot to reduce cold starts, though occasional `hibernate-wake-error` responses can still occur on Render's free tier during wake-up — a paid instance avoids this entirely.
- **CORS**: the FastAPI backend must explicitly allow the frontend's origin(s) in `CORSMiddleware`. If a route throws an unhandled exception, the response can fail to include CORS headers, which browsers report as a CORS error even though the real cause is a server-side crash — check backend logs for a traceback in that case rather than assuming it's a CORS config issue.
- **Custom domain required for OAuth verification** — see note in the Local Setup section above.

## Key Concepts

**State** — a `TypedDict` passed through every node, acting as shared memory for the agent during a task.

**Nodes** — individual units of work. Each reads from state and writes updates back.

**Conditional Edges** — routing logic between nodes. The approval node uses a conditional edge to either end the graph or loop back to redraft with feedback.

**Human-in-the-loop** — the agent pauses before sending, requiring explicit approval and capturing feedback to improve rewrites.

**OAuth 2.0** — users authenticate with Google once, token is stored in the database, and refreshed automatically on subsequent requests.

**Progressive search retry** — rather than fetching the entire mailbox up front, the search flow fetches a page of emails, filters and evaluates it, and only fetches further pages if no match is found — balancing completeness against Gmail API and LLM token cost.

## Author

Cracked-Code
[GitHub](https://github.com/Cracked-Code)
