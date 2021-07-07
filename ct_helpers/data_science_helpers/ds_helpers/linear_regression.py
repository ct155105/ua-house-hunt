import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from ct_math import algebra as alg 

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
        x: x series column name
        y: y series column name

    Returns:
        A tuple containg m, b, and the function mx+b that takes x as a parameter
    '''

    np_x, np_y = get_x_y_arrays(df,x,y)
    return predict_mx_plus_b(np_x, np_y)


# TODO This is not really a generic helper... Should probably go to a generic utilities module for the application
def get_predicted_house_price(property: dict, linear_functions: dict) -> float:
    '''Calculates the expected value of the property by calculating each dimension's expected value and averaging
    
    Args:
        property: A dictionary object with keys equal to a property dimension and value equal to the value of that dimension for the given property
        linear_functionas: a dictionary object with key equal to a dimension and value equal to the mx+b function object modeled for that dimension

    Returns:
        The predicted value of the house
    '''

    values = []

    for key in property:
        if key in linear_functions:
            values.append(linear_functions[key](property[key]))

    mean = alg.get_average_of_list_values(values)

    return mean

def get_plot_and_scatter_image(df: pd.DataFrame, x: str, y: str, output_path: str) -> None:
    '''Creates a matplotlib scatter chart with a line plot showing the linear regression model.
    Useful when doing data analysis
    
    Args:
        df: DataFrame containing the values
        x: x series column name
        y: y series column name
        output_path: path for the outputed image file

    Returns:
        None -> the function itself returns the value None, but an image is outputted to the specified location

    '''

    np_x = df[x].to_numpy()
    np_y = df[y].to_numpy()

    plt.scatter(np_x, np_y, 1)

    ln_x, ln_y = get_x_y_arrays(df, x, y)
    model = LinearRegression().fit(ln_x, ln_y)
    test_y = model.predict(ln_x)
    plt.plot(ln_x,test_y, color='black', linewidth=3)

    plt.savefig(output_path)