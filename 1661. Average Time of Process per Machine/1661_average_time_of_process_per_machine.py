import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:

    pivoted = activity.pivot_table(
        index=["machine_id", "process_id"], 
        columns="activity_type", values="timestamp"
        ).reset_index()
    
    pivoted["processing_time"] = pivoted["end"] - pivoted["start"]
    df = pivoted.groupby("machine_id")["processing_time"].mean().reset_index()
    df["processing_time"] = df["processing_time"].round(3)

    return df[["machine_id", "processing_time"]]
    