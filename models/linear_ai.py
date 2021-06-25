import pandas as pd
from pandas.core.frame import DataFrame
from models.dimension import Dimension
from ct_helpers.df_helpers.df_transformers import trim_col_names

class Linear_AI():
    '''Houses all the modeled dimensions for a DataFrame'''

    def __init__(self, df: pd.DataFrame, value_column: str):
        '''Initializes the Linear_AI
        
        Args:
            df: The DataFrame housing the data
            value_column: The name of the column that should be the Y axis
            
        '''

        df = trim_col_names(df)
        for col in df.columns:
            self.col = Dimension(df,col,value_column)
            