from langchain_google_genai import ChatGoogleGenerativeAI

from state import EmailWriter

def draft_reply(state:EmailWriter) :
    email = state['current_email']
    feedback = state['feedback']
    name = state['name']

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    prompt = f"""You are an email assistant writing on behalf of {state['account']}. Write a reply to this email. 
    From: {email['sender']}, Subject: {email['subject']}, Body: {email['body']}. If you refer in anyway the user, refer to them by {name}.
    When signing off the email, use {name}"""
    if feedback:
        prompt += f" Previous draft was rejected. Feedback: {feedback}"
    
    response = llm.invoke(prompt)

    return {"draft_reply" : response.content} 
    