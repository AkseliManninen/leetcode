# Runtime 400 ms

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    unique_duplicates = person[person.duplicated(subset="email", keep="last")]["email"].unique()
    df = pd.DataFrame(unique_duplicates, columns=["Email"])
    return df