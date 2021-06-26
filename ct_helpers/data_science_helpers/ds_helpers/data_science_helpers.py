import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def get_x_y_arrays(df: pd.DataFrame, x: str, y: str) -> tuple[np.array, np.array]:
    '''Returns a tuple of numpy arrays from dataframe to easily transform dataframe for data science library processing
    
    Args:
        df: The DataFrame containing the x and y values
        x: Column name for the x series
        y: Column name for y series

    Returns:
        A tuple containg the x and y series as np arrays 
    '''

    np_array_x = df[x].to_numpy()
    np_array_y = df[y].to_numpy()
    x = np_array_x.reshape((-1,1))
    y = np_array_y

    return (x, y)


def predict_mx_plus_b(x: np.array, y: np.array) -> tuple[float, float, object]:
    '''Pass in the array of x values and array of y values to get an object containg the prediceted slope, intercept, 
    and a function for passing x to 'y=mx+b' based on the predicted model
    
    Args:
        x: x series
        y: y series

    Returns:
        A tuple containg m, b, and the function mx+b that takes x as a parameter
    '''

    model = LinearRegression().fit(x,y)
    m = round(model.coef_[0],5)
    b = round(model.intercept_,5)
    def mx_b(x1):
        return (m*x1) + b

    return (m, b, mx_b)


def predict_mx_plus_b_from_df(df: pd.DataFrame, x: str, y: str) -> tuple[float, float, object]:
    '''Pass in the DataFrame, name of the x column, and name of the y column to predict the slope, intercept, 
    and a function for passing x to 'y=mx+b'
    
    Args:
        df: DataFrame containing the values
        x: x series
        y: y series

    Returns:
        A tuple containg m, b, and the function mx+b that takes x as a parameter
    '''

    np_x, np_y = get_x_y_arrays(df,x,y)
    return predict_mx_plus_b(np_x, np_y)