from langchain_google_genai import ChatGoogleGenerativeAI
from state import EmailWriter

def select_email(state: EmailWriter):
    emails = state["emails"]
    index = None
    if not emails:
        print("No unread emails found.")
        return {"completed": True}
    
    userinput = input("Hi! What email are you looking for? ")

    while index is None:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        prompt = f"Here are the emails with their index numbers: {list(enumerate(emails))}. The user is looking for: {userinput}. Return the 3 best matches showing their ORIGINAL INDEX NUMBER from the list, the sender, and subject. Keep it brief."
        
        response = llm.invoke(prompt)
        print(response.content)
        
        userinput2 = input("\nWhich one would you like to respond to? Type the number associated with the email or 0 to search again:\n ")
        choice = int(userinput2)
        if choice == 0:
            userinput = input("What are you looking for? ")  # let them search again
        else:
            index = choice   # valid pick, exit loop
        
    return {"current_email": state["emails"][index]}