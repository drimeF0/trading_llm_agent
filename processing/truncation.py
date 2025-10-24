from typing import Tuple
import pandas as pd


def truncate_timerange_by(df0: pd.DataFrame, df1: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    start_date = max(df0.index.min(), df1.index.min())
    end_date = min(df0.index.max(), df1.index.max())

    # Filter dataframes to the common time range
    df0 = df0.loc[start_date:end_date]
    df1 = df1.loc[start_date:end_date]
    return df0, df1

