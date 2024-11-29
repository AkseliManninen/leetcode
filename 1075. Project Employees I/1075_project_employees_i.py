import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df_merged = project.merge(employee, on="employee_id")
    df_grouped = df_merged[["project_id", "experience_years"]].groupby(by="project_id", as_index=False).mean().round(2)
    df = df_grouped.rename(columns={"experience_years": "average_years"})
    return df