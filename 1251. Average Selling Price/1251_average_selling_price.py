import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:

    merged = pd.merge(units_sold, prices, on="product_id")
    merged = merged[(merged["purchase_date"] >= merged["start_date"]) & 
                        (merged["purchase_date"] <= merged["end_date"])]

    merged["revenue"] = merged["units"] * merged["price"]

    total_revenue = merged.groupby("product_id")["revenue"].sum().reset_index(name="total_revenue")
    total_units = merged.groupby("product_id")["units"].sum().reset_index(name="total_units")

    result = pd.merge(total_revenue, total_units, on="product_id")
    result["average_price"] = result["total_revenue"] / result["total_units"]

    all_products = pd.DataFrame(prices["product_id"].unique(), columns=["product_id"])
    result = pd.merge(all_products, result, on="product_id", how="left").fillna(0)
    result["average_price"] = result["average_price"].round(2)

    return result[["product_id", "average_price"]]