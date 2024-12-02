import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    ids = employees["employee_id"].unique()
    df = employees[~(employees["manager_id"].isin(ids) | employees["manager_id"].isna())]
    df = df[df["salary"] < 30000]
    df = df.sort_values(by="employee_id")
    return df[["employee_id"]]