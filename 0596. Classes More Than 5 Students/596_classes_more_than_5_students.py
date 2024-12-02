import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by="class", as_index=False).count()
    return df[df["student"] >= 5][["class"]]
    