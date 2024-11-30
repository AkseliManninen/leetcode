import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders["order_date"].apply(
            lambda x: 
            pd.to_datetime(x) >= pd.to_datetime("2020-02-01") and
            pd.to_datetime(x) < pd.to_datetime("2020-03-01")
        )
    ]

    orders = orders[["product_id", "unit"]].groupby(by="product_id", as_index=False).sum()

    df = orders.merge(products, on="product_id", how="left")
    df = df[df["unit"] >= 100]

    return df[["product_name", "unit"]]