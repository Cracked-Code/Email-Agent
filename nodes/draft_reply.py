from langchain_google_genai import ChatGoogleGenerativeAI

from state import EmailWriter

def draft_reply(state:EmailWriter) :
    email = state['current_email']
    feedback = state['feedback']

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    prompt = f"You are an email assistant writing on behalf of {state['account']}. Write a reply to this email. From: {email['sender']}, Subject: {email['subject']}, Body: {email['body']}."
    if feedback:
        prompt += f" Previous draft was rejected. Feedback: {feedback}"
    
    response = llm.invoke(prompt)

    return {"draft_reply" : response.content} 
    