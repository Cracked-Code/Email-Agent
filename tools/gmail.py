from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
from database import User

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service(account: str, db):
    
    user = db.query(User).filter(User.account_name == account).first()
    if not user:
        raise ValueError(f"No account found for {account}. Please connect via /auth/login")
    token_json = user.token_json  # access the field from the user object

    creds = Credentials.from_authorized_user_info(json.loads(token_json), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # Save refreshed token back
    user.token_json = creds.to_json()
    db.commit()

    return build('gmail','v1', credentials=creds)