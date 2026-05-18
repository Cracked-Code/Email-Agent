from state import EmailWriter
from email.mime.text import MIMEText
import base64
from tools.gmail import get_gmail_service

def approval(state:EmailWriter, db):
    if state["awaiting_approval"]:
        service = get_gmail_service(state["account"], db)
        message = send_email(state["current_email"]["sender"], state["current_email"]["subject"], state["draft_reply"])
        service.users().messages().send(userId='me', body=message).execute()
        return {"completed": True}
    else:
        return {"completed": False, "feedback": state["feedback"]}


def send_email(to, subject, body) :
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = "Re: " + subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}
    

