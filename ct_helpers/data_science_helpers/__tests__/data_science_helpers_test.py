import pandas as pd
import numpy as np 
import ct_helpers.data_science_helpers.data_science_helpers as ds


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
    #2 = .5(2) + 1
    assert test[2](2) == 2
