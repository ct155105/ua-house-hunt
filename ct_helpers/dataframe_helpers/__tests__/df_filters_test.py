import df_helpers.df_filters as ct
import pandas as pd
import numpy as np

d = {'test_col_1': ['foo','bar','baz','foo','bar','foo','foofoo', np.NaN], 
    'test_col_2': ['test1','test2','test3','test4','test5','test6','test7',np.NaN], 
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


def test_remove_nan_from_columns():
    data = {'col1': [0,1,np.NaN,2,3], 
            'col2': [np.NaN, 'string1', 'string2','string3','string3'],
            'col3': [0,1,2,3,4] }
    df = pd.DataFrame(data)
    df2 = ct.remove_nan_from_columns(df, 'col1','col2')

    assert df['col3'].tolist() == [0,1,2,3,4]
    assert df2['col3'].tolist() == [1,3,4]