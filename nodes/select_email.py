from langchain_google_genai import ChatGoogleGenerativeAI
from state import EmailWriter

def prefilter_emails(emails, query):
    """Cheap local keyword filter — no API calls, no tokens."""
    query_terms = query.lower().split()
    candidates = []
    for i, e in enumerate(emails):
        haystack = f"{e.get('sender','')} {e.get('subject','')} {e.get('body','')[:500]}".lower()
        if any(term in haystack for term in query_terms):
            candidates.append((i, e))
    return candidates

def trim_email(email, max_body_chars=200):
    """Strip email down to just what the LLM needs to judge relevance."""
    return {
        "sender": email.get("sender", ""),
        "subject": email.get("subject", ""),
        "body_snippet": email.get("body", "")[:max_body_chars]
    }



def select_email(state: EmailWriter):
    emails = state["emails"]
    query = state["query"]

    if not emails:
        print("No unread emails found.")
        return {"completed": True}

    candidates = prefilter_emails(emails, query)

    if not candidates:
        # Nothing even loosely matches by keyword — skip the LLM call entirely
        return {"matches": "False", "emails": emails}

    trimmed = [(idx, trim_email(e)) for idx, e in candidates]

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    prompt = f"""Here are candidate emails with their original index numbers: {trimmed}.
    The user is looking for: {query}.
    Return the best matches as a JSON array with this exact structure:
    [{{"index": 0, "sender": "...", "subject": "..."}}]
    Return ONLY the JSON array, no other text, no markdown backticks.
    If none are genuinely relevant, return "False"."""

    response = llm.invoke(prompt)
    return {"matches": response.content, "emails": emails}