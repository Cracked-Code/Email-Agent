from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from database import get_db, User
from google_auth_oauthlib.flow import Flow
import os
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

router = APIRouter()
SCOPES = [
    'https://www.googleapis.com/auth/gmail.modify',
    'openid',
    'https://www.googleapis.com/auth/userinfo.email'
]
# Query parameters in FastAPI
@router.get("/login")
def login(account: str, request: Request):
    flow = Flow.from_client_secrets_file('credentials.json', SCOPES)
    flow.redirect_uri = "https://email-agent-api-bvjy.onrender.com/auth/callback"
    auth_url, state = flow.authorization_url(state=account, access_type="offline", include_granted_scopes="true",prompt="consent")
    request.session["code_verifier"] = flow.code_verifier
    return RedirectResponse(url=auth_url)


# Receiving the code from Google
@router.get("/callback")
def callback(code: str, state: str, request: Request, db: Session = Depends(get_db)):
    flow = Flow.from_client_secrets_file('credentials.json', SCOPES, state=state)
    flow.redirect_uri = "https://email-agent-api-bvjy.onrender.com/callback"
    
    authorization_response = str(request.url)
    flow.fetch_token(
    authorization_response=authorization_response,
    code_verifier=request.session.get("code_verifier")
    )       
    creds = flow.credentials
    token_json = creds.to_json()
    
    id_info = id_token.verify_oauth2_token(
    creds.id_token,
    google_requests.Request()
    )
    email = id_info["email"]
    
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        existing_user.token_json = token_json
        db.commit()
    else:
        user = User(email=email, account_name=state, token_json=token_json)
        db.add(user)
        db.commit()
    
    # Redirecting back to frontend
    return RedirectResponse(url=f"http://localhost:3000?account={state}")