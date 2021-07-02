import pandas as pd
import numpy as np 
import ds_helpers.linear_regression as ds

def test_get_numpy_x_y_from_df():
    d = {"col1": [1,2,3], "col2": [4,5,6]}
    df = pd.DataFrame(d)
    x, y = ds.get_x_y_arrays(df, 'col1', 'col2')
    x_truthy =  x == np.array([[1],[2],[3]])
    y_truthy = y == np.array([4, 5, 6])
    assert x_truthy.all() and y_truthy.all()

def test_predict_mx_plusb():
    x = np.array([[0],[2],[4]])
    y = np.array([1,2,3])
    
    test = ds.predict_mx_plus_b(x,y)
    #slope should equal .5
    assert test[0] == .5
    #intercept should equal 1
    assert test[1] == 1
    #y = .5x + 1
    #2 = .5(6) + 1
    assert test[2](6) == 4

def test_predict_mx_plus_b_from_df():
    d = {"col1": [1,2,3], "col2": [4,5,6]}
    df = pd.DataFrame(d)
    test = ds.predict_mx_plus_b_from_df(df,'col1','col2')
    #slope should equal 1
    assert test[0] == 1
    #intercept should equal 3
    assert test[1] == 3
    #y = 1x + 3
    #2 = 1(2) + 3
    assert test[2](2) == 5


def test_get_predicted_house_price():
    prop = { "acres": 10, "rooms": 5, "basement": 0, "NA": 100 }

    #mock y = mx + b for the dimensions
    def mock_acres_line(x):
        y = (100*x) + 1000
        return y
    def mock_rooms_line(x):
        y = (50*x) + 500
        return y
    def mock_basement_line(x):
        y = (200*x) + 10
        return y

    
    lf = { "acres": mock_acres_line, "rooms": mock_rooms_line, "basement": mock_basement_line }

    predicted = ds.get_predicted_house_price(prop, lf)

    assert predicted == 920