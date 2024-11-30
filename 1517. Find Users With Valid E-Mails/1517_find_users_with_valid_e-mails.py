import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def is_valid(email):
        if not email.endswith("@leetcode.com"):
            return False
        
        if not email[0].isalpha():
            return False

        if any(
            not(c.isalpha() or 
            c.isdigit() or
            c in ["_", ".", "-"]) 
            for c in email[1:-14]
        ):
            return False
        
        return True

    valid_emails = users[users["mail"].apply(is_valid)]

    return valid_emails