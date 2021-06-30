from models import linear_ai
from models.linear_ai import Linear_AI
import pandas as pd
import numpy as np

def test_linear_ai_init():
    d = {"col1": ['test1', 'test2', 'test3'], "col2": [0,1,2], "col3" : [np.NaN, 2, 4], "value_col": [1,2,3]}
    df = pd.DataFrame(d)
    ai = Linear_AI(df, 'value_col')

    assert not hasattr(ai, 'col1')
    assert hasattr(ai, 'col2')
    assert hasattr(ai, 'col3')
    
    assert 'col1' in ai.error_columns.keys()
    assert 'col2' not in ai.error_columns.keys()
    assert 'col3' not in ai.error_columns.keys()