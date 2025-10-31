import datetime
from typing import List, Optional
import pandas as pd
import numpy as np




class DataSource:

    def __init__(self, preprompt: str = ""):
        pass

    
    def at(self, datatime: datetime.datetime):
        raise NotImplementedError





class Dataset:
    
    def __init__(self):
        self.sources: List[DataSource] = []
    

    def add_source(self, source: DataSource):
        self.sources.append(source)



