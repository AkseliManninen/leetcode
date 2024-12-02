import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.drop_duplicates(keep=False)
    if len(df) > 0:
        return df[df["num"] == df["num"].max()][["num"]]
    else:
        return pd.DataFrame({"num": [nan]})