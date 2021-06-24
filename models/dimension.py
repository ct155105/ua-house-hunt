import ct_helpers
import pandas as pd
import numpy as np
from ct_helpers.data_science_helpers import data_science_helpers as ds
from ct_helpers.df_helpers import df_filters as df

class Dimension():
    def __init__(self, df: pd.DataFrame, x_column: str, y_column: str):
        '''Stores mx+b equation for a given dimension

        Args:
            df: DataFrame containing the dimension.
            x_column: Column name for the dimension.
            y_column: Nae of column storing the values for the dimension
        '''

        dim = ds.predict_mx_plus_b_from_df(df,x_column,y_column)

        self._m = dim[0]
        self._b = dim[1]
        self._calc = dim[2]

    @property
    def m(self):
        '''Get the slope for the dimension'''
        return self._m
        
    @property
    def b(self):
        '''Get the Y intercept for the dimension'''
        return self._b

    def calc(self, x):
        """Predicts the Y value based on the inputted X value for a given dimension

        Args:
            x: The dimension's characteristic

        Returns:
            The predicted value corresponding to the dimension

        """
    
        return self._calc(x)