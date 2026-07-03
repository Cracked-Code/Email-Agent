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
    account: str 

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
def search_email(request:SearchEmailInquiry, db: Session = Depends(get_db)):
    import json
    if not request.emails:
        return {"matches": []}
    state = {
        "emails" : request.emails,
        "current_email": None,
        "draft_reply": None,
        "action_taken": None,
        "awaiting_approval": False,
        "completed": False,
        "feedback": None,
        "account": request.account,
        "name": "",
        "query" : request.query
    }
    result = select_email(state) 
    raw_matches = result.get("matches")
    
    count = 0
    page_token = None
    while(raw_matches == "False" and count < 10) :
        print("\nThis is count : " , count)

        fetch_result = fetch_emails(state, db, page_token=page_token)
        page_token = fetch_result.get("next_page_token")
        state["emails"] = fetch_result["emails"]

        result = select_email(state)
        raw_matches = result.get("matches")
        count += 1

        print("This is the emails pulled :\n", raw_matches)
        if not page_token:
            break   
    if raw_matches is None:
        matches = []
    elif isinstance(raw_matches, str):
        try:
            matches = json.loads(raw_matches)
        except json.JSONDecodeError:
            matches = []
    else:
        matches = raw_matches  # already a list/dict, use as-is

    if not isinstance(matches, list):
        matches = []

    return {"matches": matches}

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