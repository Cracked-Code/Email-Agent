from state import EmailWriter
from tools.gmail import get_gmail_service
import base64

def fetch_emails(state:EmailWriter) :
    gmail_service = get_gmail_service(state["account"])

    result = gmail_service.users().messages().list(userId='me', labelIds=['UNREAD'],maxResults = 10 ).execute()
    message = result.get('messages', [])

    emails = []
    for msg in message :
        mail = gmail_service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        emails.append(parse_email(mail))

    return {"emails" : emails}

def parse_email(message):
    headers = message["payload"]["headers"]
    subject = None
    sender = None
    for msg in headers :
        if msg["name"] == "Subject" :
            subject = msg["value"]
        if msg["name"] == "From" :
            sender = msg["value"]
    
    body_data = message["payload"].get("body", {}).get("data", "")
    if not body_data:
        parts = message["payload"].get("parts", [])
        if parts:
            body_data = parts[0].get("body", {}).get("data", "")

    body = base64.urlsafe_b64decode(body_data).decode("utf-8") if body_data else ""
    
    return {"subject": subject, "sender" :sender, "id" : message["id"], "body" : body}
    