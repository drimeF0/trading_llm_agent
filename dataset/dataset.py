import datetime
from typing import List, Optional
import pandas as pd
import numpy as np




class DataSource:

    def __init__(self, preprompt: str = ""):
        self.prepompt = preprompt

    
    def at(self, datetime_: datetime.datetime) -> str:
        raise NotImplementedError


class PandasDataSource(DataSource):

    def __init__(self, df: pd.DataFrame, n: int = 1, *args, **kwargs):
        self.df = df
        self.n = n

        super().__init__(*args, **kwargs)
    
    
    def _at(self, datetime_: datetime.datetime, n: int = 1) -> pd.DataFrame:
        df = self.df.loc[datetime_:]
        df = df.head(n)
        return df



class RetailTGDataSource(PandasDataSource):

    def at(self, datetime_: datetime.datetime) -> str:


        df = self._at(datetime_, self.n)
        

        return_string = f"{self.prepompt}\n"

        for username, message_text, message_date in zip(df["username"], df["message_text"], df["message_date"]):
            msg_string = f"{message_date}{username}: {message_text}\n"
            return_string += msg_string
        
        return return_string







class Dataset:
    
    def __init__(self):
        self.sources: List[DataSource] = []
    

    def add_source(self, source: DataSource):
        self.sources.append(source)

if __name__ == "__main__":
    pass

