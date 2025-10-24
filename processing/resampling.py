import pandas as pd

def resample_to_daily(df: pd.DataFrame, separator: str = "\n[NEXT]\n", column: str = "text") -> pd.DataFrame:
    daily_df = df.resample('D').agg({
        column: separator.join
    })
    return daily_df