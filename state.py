from typing import TypedDict, Optional, List


class EmailWriter(TypedDict) :
    emails : List[dict]
    current_email : Optional[dict]
    draft_reply : Optional[str]
    action_taken : Optional[str]
    awaiting_approval : bool
    completed : bool
    feedback : Optional[str]
    account: Optional[str]