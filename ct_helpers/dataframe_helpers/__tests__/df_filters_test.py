import df_helpers.df_filters as ct
import pandas as pd

d = {'test_col_1': ['foo','bar','baz','foo','bar','foo','foofoo', None], 
    'test_col_2': ['test1','test2','test3','test4','test5','test6','test7',None], 
    'test_col_3': [0,1,2,3,4,5,6,7]}

def test_string_exact():
    df = pd.DataFrame(d)
    filtered = ct.string_column(df,'test_col_1','foo',True)
    assert filtered.shape[0] == 3

def test_string_contains():
    df = pd.DataFrame(d)
    filtered = ct.string_column(df,'test_col_1','foo')
    assert filtered.shape[0] == 4

def test_zeros_filter():
    df = pd.DataFrame(d)
    filtered = ct.remove_zeros(df,'test_col_3')
    assert filtered.shape[0] == 7