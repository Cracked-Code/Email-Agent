from state import EmailWriter
from email.mime.text import MIMEText
import base64
from tools.gmail import get_gmail_service

def approval(state:EmailWriter):
    response = state['draft_reply']
    print(response)

    user_input=input("Do you approve this reply? Y/N : ")

    if user_input == "Y" or user_input == "y" :
        service = get_gmail_service(state["account"])
        message = send_email(state["current_email"]["sender"], state["current_email"]["subject"], state["draft_reply"])
        service.users().messages().send(userId='me', body=message).execute()
        print("Done!")
        return {"completed" : True}
    else :
        feedback = input("What should be changed? ")
        return {"completed" : False, "feedback" : feedback}


def send_email(to, subject, body) :
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = "Re: " + subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}
    

