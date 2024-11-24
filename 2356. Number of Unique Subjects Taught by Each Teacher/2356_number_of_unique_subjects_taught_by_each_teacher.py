import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher[["teacher_id", "subject_id"]].drop_duplicates()
    df = df.groupby(by=["teacher_id"]).size().reset_index()
    df = df.rename(columns={0: "cnt"})
    return df