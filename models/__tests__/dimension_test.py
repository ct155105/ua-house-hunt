from models.dimension import Dimension as dm
import pandas as pd

def test_dimension_constructor():
    data = {"rooms": [0,1,2], "SalePrice": [4000,5000,6000], "footage": [0,1000,2000]}
    df = pd.DataFrame(data)

    dim = dm(df,"rooms", "SalePrice")

    #slope should be 1000
    assert dim.m == 1000
    #intercept should be 400
    assert dim.b == 4000
    #y = 1000x + 4000
    #y = 1000(3) + 4000
    assert dim.calc(3) == 7000
