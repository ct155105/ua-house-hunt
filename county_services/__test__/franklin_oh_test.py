import pandas as pd
import numpy as np
import pytest
from county_services.oh import franklin as fkoh

nrows = 1000
df = pd.read_csv('data/oh/franklin/Parcel_Boundaries.csv', nrows=nrows)


def test_franklin_resi_filter():
    result = fkoh.get_resi(df)
    assert result.shape[0] < nrows 
    assert result.shape[0] > 0


def test_get_neighborhood_code():
    test = fkoh.get_neighborhood_code('Upper Arlington')
    assert test == 70

    with pytest.raises(Exception) as e_info:
        fkoh.get_neighborhood_code('Does Not Exist')


def test_get_neighborhood_code():
    data = {"CVTTXCD": [70,70,180,180]}
    df = pd.DataFrame(data)
    test = fkoh.get_neighborhood(df, 'Upper Arlington')
    assert test.shape[0] == 2

    with pytest.raises(Exception) as e_info:
        fkoh.get_neighborhood(df, 'Does Not Exist')


def test_get_attic_cd():
    test = fkoh.get_attic_cd('NO ATTIC')
    assert test  == 0
    test = fkoh.get_attic_cd('ATTIC UNF')
    assert test  == 1
    test = fkoh.get_attic_cd('1/2 ATTIC FINISH')
    assert test  == 2
    test = fkoh.get_attic_cd('3/4 ATTIC FINISH')
    assert test  == 3
    test = fkoh.get_attic_cd('FULL ATTIC FINISH')
    assert test  == 4 
    test = fkoh.get_attic_cd('DOES NOT MATCH')
    assert np.isnan(test) 


def test_attic_cd_append():
    d = {'test': ['NO ATTIC','NO ATTIC','ATTIC UNF','1/2 ATTIC FINISH','3/4 ATTIC FINISH','FULL ATTIC FINISH','DOES NOT MATCH'], 'ATTIC': ['NO ATTIC','NO ATTIC','ATTIC UNF','1/2 ATTIC FINISH','3/4 ATTIC FINISH','FULL ATTIC FINISH','DOES NOT MATCH']}
    df = pd.DataFrame(d)
    df = fkoh.append_attic_cd(df)
    values = df['attic_cd'].values.tolist() 
    
    assert values[0] == 0
    assert values[1] == 0
    assert values[2] == 1
    assert values[3] == 2
    assert values[4] == 3
    assert values[5] == 4
    assert np.isnan(values[6])
    
