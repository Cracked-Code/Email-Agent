from graph import graph
from dotenv import load_dotenv


load_dotenv()

def main() :
    graph.invoke({
    "emails": [],
    "current_email": None,
    "draft_reply": None,
    "action_taken": None,
    "awaiting_approval": False,
    "completed": False,
    "feedback": None
})

if __name__ == "__main__":
    main()