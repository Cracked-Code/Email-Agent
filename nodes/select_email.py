from langchain_google_genai import ChatGoogleGenerativeAI
from state import EmailWriter

def select_email(state: EmailWriter):
    emails = state["emails"]
    
    if not emails:
        print("No unread emails found.")
        return {"completed": True}
    
    userinput = input("Hi! What email are you looking for? ")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    prompt = f"Here are the emails: {emails}. The user is looking for: {userinput}. Return the 3 best matches. For each one show the number (1, 2, or 3), the sender, and the subject. Keep it brief."
    
    response = llm.invoke(prompt)
    print(response.content)
    
    userinput2 = input("Which one would you like to respond to? (1, 2, or 3) ")
    index = int(userinput2) - 1
    
    return {"current_email": state["emails"][index]}