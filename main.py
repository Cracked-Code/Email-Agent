from graph import graph
from dotenv import load_dotenv

load_dotenv()

def main():
    graph.invoke({
        "emails": [],
        "current_email": None,
        "draft_reply": None,
        "action_taken": None,
        "awaiting_approval": False,
        "completed": False,
        "feedback": None,
        "account": input("What email account do you wish to use? "),
        "name": input("What would you like to be referred to? ")
    })
    
if __name__ == "__main__":
    main()