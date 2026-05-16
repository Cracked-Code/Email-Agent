from langchain_google_genai import ChatGoogleGenerativeAI

from state import EmailWriter

def think(state:EmailWriter) :
    emails = state["emails"]
    first_email = emails[0]

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response = llm.invoke(f"You are an email assistant. From: {first_email['sender']}, Subject: {first_email['subject']}, Body: {first_email['body']}. What action should be taken?")
    
    return {"action_taken": response.content, "current_email" : first_email}