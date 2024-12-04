import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.sort_values(by=["employee_id", "primary_flag"], ascending=False)
    df = df.drop_duplicates(subset="employee_id")
    return df[["employee_id", "department_id"]]
    