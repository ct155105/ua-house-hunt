import pandas as pd
from county_services.oh import franklin as fkoh

nrows = 1000
df = pd.read_csv('data/oh/franklin/Parcel_Boundaries.csv', nrows=nrows)

def test_franklin_resi_filter():
    result = fkoh.filter_residential(df)
    assert result.shape[0] < nrows 
    assert result.shape[0] > 0