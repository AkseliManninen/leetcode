import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_subjects = pd.merge(students, subjects, how="cross")

    examinations["attended_exams"] = examinations.groupby(["student_id", "subject_name"])["subject_name"].transform("count")
    examinations = examinations.drop_duplicates(subset=["student_id", "subject_name"])

    merged_df = pd.merge(student_subjects, examinations, on=["student_id", "subject_name"], how="left")
    merged_df["attended_exams"] = merged_df["attended_exams"].fillna(0).astype(int)

    df = merged_df[["student_id", "student_name", "subject_name", "attended_exams"]]
    df = df.sort_values(by=["student_id", "subject_name"])

    return df
    