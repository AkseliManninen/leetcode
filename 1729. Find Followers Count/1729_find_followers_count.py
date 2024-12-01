import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    df = followers.groupby(by="user_id", as_index=False).count()
    df = df.rename(columns={"follower_id": "followers_count"})
    
    return df
    