import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    num_users = len(users["user_id"].unique())
    df = register.groupby(by="contest_id", as_index=False).count()
    df["percentage"] = df["user_id"].apply(lambda x: round((x / num_users), 4) * 100)
    df = df[["contest_id", "percentage"]]
    df = df.sort_values(by=["percentage", "contest_id"], ascending=[False, True])
    return df
