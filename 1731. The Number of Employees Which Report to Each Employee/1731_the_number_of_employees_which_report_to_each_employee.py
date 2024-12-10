import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    managers = employees[["reports_to", "employee_id"]].groupby(by="reports_to", as_index=False).count()
    managers = managers.rename(columns={"reports_to": "employee_id", "employee_id": "reports_count"})
    managers = managers.merge(employees[["employee_id", "name"]], on="employee_id", how="left")
    ages = employees[["reports_to", "age"]].groupby(by="reports_to", as_index=False).mean()
    ages["age"] = ages["age"].apply(lambda x: floor(x+0.5)) 
    managers = managers.merge(ages, left_on="employee_id", right_on="reports_to", how="left")
    managers = managers.rename(columns={"age": "average_age"})
    return managers[["employee_id", "name", "reports_count", "average_age"]]
    