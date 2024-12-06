import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    bools = triangle.apply(lambda row: 
        2 * max(row["x"], row["y"], row["z"]) < sum([row["x"], row["y"], row["z"]]), axis=1
    )
    bools = bools.map({True: "Yes", False: "No"})
    triangle["triangle"] = bools

    return triangle
    