from langgraph.graph import StateGraph, START, END
from state import EmailWriter
from nodes.approve import approval
from nodes.draft_reply import draft_reply
from nodes.fetch_emails import fetch_emails
from nodes.think import think
from nodes.select_email import select_email

graph = StateGraph(EmailWriter)

graph.add_node("fetch_emails", fetch_emails)
graph.add_node("select_email", select_email)
graph.add_node("think", think)
graph.add_node("draft_reply", draft_reply)
graph.add_node("approval", approval)

graph.add_edge(START, "fetch_emails")
graph.add_edge("fetch_emails", "select_email")
graph.add_conditional_edges(
    "select_email",
    lambda state: "end" if state["completed"] else "think",
    {"end": END, "think": "think"}
)
graph.add_edge("think", "draft_reply")
graph.add_edge("draft_reply", "approval")
graph.add_conditional_edges(
    "approval",
    lambda state: "end" if state["completed"] else "draft_reply",
    {"end": END, "draft_reply": "draft_reply"}
)

graph = graph.compile()