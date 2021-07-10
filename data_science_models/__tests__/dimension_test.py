from models.dimension import Dimension as dm
import pandas as pd
import numpy as np
import pytest


def test_dimension_init():
    data = {"rooms": [0,1,2,np.NaN,10], "SalePrice": [4000,5000,6000,7000,np.NaN], "footage": [0,1000,2000,3000,4000]}
    df = pd.DataFrame(data)

    dim = dm(df,"rooms", "SalePrice")

    #slope should be 1000
    assert dim.m == 1000
    #intercept should be 400
    assert dim.b == 4000
    #y = 1000x + 4000
    #y = 1000(3) + 4000
    assert dim.calc(3) == 7000

    assert dim.mean == 5000

    #check for empty dataframe
    with pytest.raises(Exception) as e_info:
        data = {"rooms": [np.NaN,np.NaN,np.NaN], "SalePrice": [4000,5000,6000]}
        df = pd.DataFrame(data)
        dim = dm(df,"rooms", "SalePrice")