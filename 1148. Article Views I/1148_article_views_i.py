import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views["id"] = views["author_id"]
    views = views[views["author_id"] == views["viewer_id"]]
    df_id = views[["id"]].drop_duplicates().sort_values(by="id")
    return df_id