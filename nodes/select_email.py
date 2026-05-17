from langchain_google_genai import ChatGoogleGenerativeAI
from state import EmailWriter

def select_email(state: EmailWriter):
    emails = state["emails"]
    query = state["query"]

    if not emails:
        print("No unread emails found.")
        return {"completed": True}
    
    userinput = query
        
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    prompt = f"""Here are the emails with their index numbers: {list(enumerate(emails))}. The user is looking for: {userinput}.
    Return the 3 best matches as a JSON array with this exact structure:
    [{{"index": 0, "sender": "...", "subject": "..."}}]
    Return ONLY the JSON array, no other text, no markdown backticks."""
        
    response = llm.invoke(prompt)        
    return {"matches": response.content, "emails": emails}