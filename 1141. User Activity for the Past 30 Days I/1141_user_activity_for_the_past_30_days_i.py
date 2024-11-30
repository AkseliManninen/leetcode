import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    filtered_activity = activity[["activity_date", "user_id"]].drop_duplicates()
    df = filtered_activity[["activity_date", "user_id"]].groupby(by="activity_date", as_index=False).count()
    df = df.rename(columns={"activity_date": "day", "user_id": "active_users"})
    df = df[
        (pd.to_datetime(df["day"]) <= pd.to_datetime("2019-07-27")) &
        (pd.to_datetime(df["day"]) >= pd.to_datetime("2019-06-28")) 
    ] 
    return df
    