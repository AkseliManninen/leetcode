import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_ids = set(product.product_key)
    customer = customer.drop_duplicates()
    customer = customer.groupby(by="customer_id", as_index=False).count()
    customer = customer[customer["product_key"] == len(product_ids)]

    return customer[["customer_id"]]
    