import pandas as pd
import numpy as np


def get_tax_value_column():
    return 'TOTVALUEBASE'


def get_resi(df: pd.DataFrame) -> pd.DataFrame:
    '''Returns only properties with BLDTYP = 'Dwelling' (residential properties)
    
    Args:
        df: The dataframe to filter

    Returns:
        The filtered DF
    '''

    filtered = df[df['BLDTYP'].str.contains('Dwelling',na=False)]
    return filtered


def get_neighborhood_code(neighborhood: str) -> int:
    '''Look up for CVTTXCD column, which is where Frankling county stores the local tax district
    
    Args:
        neighborhood: The name of the neighborhood to filter the dataframe for (supported neighborhoods below)    
            Upper Arlington -> 70
    
    Returns: 
        int: The code for the neighborhood

    raises:
        ValueError: if neightborhood is not in lookup list
    '''

    if neighborhood == 'Upper Arlington':
        return 70

    raise ValueError('The neighborhood cannot be found')


def get_neighborhood(df: pd.DataFrame, neighborhood: str) -> pd.DataFrame:
    '''Filters the DataFrame for the neighborhood (CVTTXCD code)
    
    Args:
        df: The dataframe to filter
        neighborhood: The name of the neighborhood to filter the dataframe for (see get_neighborhood_code docstring for supported neighborhoods)

    Returns:
        The filtered dataframe

    Raises:
        ValueError: If  neighborhood not in lookup list    
    '''

    cd = get_neighborhood_code(neighborhood)
    result = df[df['CVTTXCD'] == cd]  

    return result      


def get_attic_cd(attic_status: str) -> int:
    '''Gets the attic code value for the inputted string. Mappings are below:

        'NO ATTIC' = 0
        'ATTIC UNF' = 1
        '1/2 ATTIC FINISH' = 2
        '3/4 ATTIC FINISH' = 3
        'FULL ATTIC FINISH' = 4 

    Args:
        attic_status: Status of the attic in English

    Returns:
        The code for the status string    
    
    '''

    result = np.NaN

    if attic_status == 'NO ATTIC':
        result = 0
    if attic_status == 'ATTIC UNF':
        result = 1
    if attic_status == '1/2 ATTIC FINISH':
        result = 2
    if attic_status == '3/4 ATTIC FINISH':
        result = 3
    if attic_status == 'FULL ATTIC FINISH':
        result = 4 

    return result


def append_attic_cd(df: pd.DataFrame) -> pd.DataFrame:
    '''Appends a new column to the dataframe called "attic_cd" from the 'ATTIC' column
    
    Args:
        df: The dataframe to append the column to
    
    Returns:
        df with the new column appended    
    '''

    df2 = df.copy()
    df2['attic_cd'] = df2['ATTIC'].apply(lambda x: get_attic_cd(x))

    return df2