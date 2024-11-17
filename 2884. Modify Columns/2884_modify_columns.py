# Runtime: 356 ms

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:, "salary"] = employees.loc[:, "salary"] * 2
    return employees