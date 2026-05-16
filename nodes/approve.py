from state import EmailWriter

def approval(state:EmailWriter):
    response = state['draft_reply']
    print(response)

    user_input=input("Do you approve this reply? Y/N : ")

    if user_input == "Y" or user_input == "y" :
        return {"completed" : True}
    else :
        feedback = input("What should be changed? ")
        return {"completed" : False, "feedback" : feedback}
    
    

