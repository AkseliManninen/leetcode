import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    df = activities.groupby("sell_date").apply(
        lambda x: pd.Series({
            "num_sold": x["product"].nunique(),
            "products": ",".join(sorted(x["product"].unique()))
        })
    ).reset_index()

    df = df.sort_values("sell_date")
    return df
    