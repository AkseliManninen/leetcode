import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(visits, transactions, on="visit_id", how="outer")
    trans_visits = df[df["amount"].notna()]["visit_id"].unique()    
    df = df[~df["visit_id"].isin(trans_visits)]    
    df["count_no_trans"] = 1    
    df = df.drop(["visit_id", "transaction_id", "amount"], axis=1)    
    df = df.groupby(by="customer_id", as_index=False).sum()
    
    return df
    