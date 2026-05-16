# Email Agent 🤖

An autonomous AI email assistant built with LangGraph and the Gmail API. The agent fetches unread emails, reasons about them, drafts replies, and asks for human approval before taking action — all in a stateful, looping graph.

## Demo

The agent:
1. Connects to your Gmail inbox via OAuth
2. Fetches unread emails and parses them cleanly
3. Uses an LLM to analyze the email and decide on an action
4. Drafts a reply
5. Presents the draft for human approval
6. If rejected, captures feedback and rewrites the draft
7. Loops until approved

## Tech Stack

- **LangGraph** — agent orchestration and stateful graph execution
- **LangChain** — LLM integration
- **Google Gemini 2.5 Flash Lite** — language model
- **Gmail API** — email fetching and OAuth authentication
- **Python** — core language

## Project Structure

```
email_agent/
├── main.py               # Entry point
├── state.py              # EmailWriter TypedDict (shared agent state)
├── graph.py              # LangGraph graph definition
├── config.py             # Environment variable loading
├── nodes/
│   ├── fetch_emails.py   # Fetches and parses unread Gmail messages
│   ├── think.py          # LLM reasons about the email
│   ├── draft_reply.py    # LLM drafts a reply (with feedback loop)
│   └── approve.py        # Human-in-the-loop approval node
└── tools/
    └── gmail.py          # Gmail OAuth service connection
```

## Agent Graph

```
START
  ↓
fetch_emails
  ↓
think
  ↓
draft_reply
  ↓
approval ──── approved ──→ END
  ↑                         
  └──── rejected (with feedback) ──→ draft_reply
```

## Setup

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

### 3. Install dependencies

```bash
pip install langgraph langchain-google-genai google-auth google-auth-oauthlib google-api-python-client python-dotenv
```

### 4. Set up Google Cloud credentials

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project and enable the **Gmail API**
3. Create **OAuth 2.0 credentials** (Desktop app)
4. Download the credentials JSON and save it as `credentials.json` in the project root

### 5. Set up environment variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your Gemini API key at [aistudio.google.com](https://aistudio.google.com).

### 6. Run the agent

```bash
python main.py
```

A browser window will open for Gmail authentication on first run. After that, `token.json` will be saved locally for future runs.

## Key Concepts

**State** — a `TypedDict` passed through every node, acting as the agent's working memory for the duration of a task.

**Nodes** — individual units of work (fetch, think, draft, approve). Each reads from state and writes updates back.

**Edges** — routing logic between nodes. The approval node uses a conditional edge to either end the graph or loop back to redraft.

**Human-in-the-loop** — the agent pauses before sending and requires explicit approval, capturing feedback if rejected to improve the next draft.

## What's Next

- [ ] Actually send approved emails via Gmail API
- [ ] Process multiple emails in one run
- [ ] Add logging and audit trail
- [ ] Calendar integration for scheduling requests

## Author

Nicholas Chopliani 
[GitHub](https://github.com/Cracked-Code)
