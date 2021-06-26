import pandas as pd

def filter_residential(df: pd.DataFrame) -> pd.DataFrame:
    '''Returns only properties with BLDTYP = 'Dwelling' (residential properties)
    
    Args:
        df: The dataframe to filter

    Returns:
        The filtered DF
    '''

    filtered = df[df['BLDTYP'].str.contains('Dwelling',na=False)]
    return filtered

def get_tax_value_column():
    return 'TOTVALUEBASE'

