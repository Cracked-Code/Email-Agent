from pydantic import BaseModel
from nodes.fetch_emails import fetch_emails
from nodes.select_email import select_email
from nodes.draft_reply import draft_reply
from nodes.approve import approval
from typing import List
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

class FetchEmailsRequest(BaseModel):
    account: str
    name: str

class SearchEmailInquiry(BaseModel):
    emails : List[dict]
    query : str

class DraftEmailRequest(BaseModel):
    name : str
    account : str
    current_email : dict
    feedback : str | None = None

class ApprovalEmail(BaseModel):
    account : str
    name : str
    current_email : dict
    draft_reply : str
    approval : bool
    feedback : str | None = None

@router.post("/fetch-emails")
def fetch_emails_endpoint(request: FetchEmailsRequest,db: Session = Depends(get_db)):
    state = {
        "emails": [],
        "current_email": None,
        "draft_reply": None,
        "action_taken": None,
        "awaiting_approval": False,
        "completed": False,
        "feedback": None,
        "account": request.account,
        "name": request.name
    }
    result = fetch_emails(state, db)
    return {"emails": result["emails"]}

@router.post("/search-email")
def search_email(request:SearchEmailInquiry ):
    import json
    state = {
        "emails" : request.emails,
        "current_email": None,
        "draft_reply": None,
        "action_taken": None,
        "awaiting_approval": False,
        "completed": False,
        "feedback": None,
        "account": "",
        "name": "",
        "query" : request.query
    }
    result = select_email(state)
    try :
        matches = json.loads(result["matches"])
    except (json.JSONDecodeError, KeyError):
        matches = result["matches"]
    return {"matches" : matches}

@router.post("/draft-reply")
def draft_email(request:DraftEmailRequest):
    state = {
        "emails" : [],
        "current_email": request.current_email,
        "draft_reply": None,
        "action_taken": None,
        "awaiting_approval": False,
        "completed": False,
        "feedback": request.feedback,
        "account": request.account,
        "name": request.name,
        "query" : ""
    }
    result = draft_reply(state)
    return {"draft_reply" :  result["draft_reply"]}

@router.post("/approve")
def approval_endpoint(request:ApprovalEmail ,db: Session = Depends(get_db)):
    state = {
        "emails" : [],
        "current_email": request.current_email,
        "draft_reply": request.draft_reply,
        "action_taken": None,
        "awaiting_approval": request.approval,
        "completed": False,
        "feedback": request.feedback,
        "account": request.account,
        "name": request.name,
        "query" : ""
    }
    result = approval(state, db)
    return {"completed" : result["completed"], "feedback" : result.get("feedback") }