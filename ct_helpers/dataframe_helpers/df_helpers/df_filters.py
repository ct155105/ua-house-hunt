import pandas as pd


def string_column(df: pd.DataFrame, column: str, value: str, exact: bool = False) -> pd.DataFrame:
    """Filters DataFrame string column by the specified value

    Args:
        df: The DataFrame to filter
        column: The column to filter on
        value: The string to filter on. TODO add list option for multiple strings
        exact: The value must match exactly. Can be substring if false.

    Returns:
        the original dataframe filtered
    """

    if exact:
        result = df[df[column].eq(value)]
        return result

    result = df[df[column].str.contains(value,na=False)]
    return result


def remove_zeros(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Filters DataFrame for zero values in the specified column

    Args:
        df: The DataFrame to filter
        column: Name of the column containing zeros

    returns:
        the filtered dataframe
    """

    result = df[df[column] > 0]
    return result


def remove_nan_from_columns(df: pd.DataFrame, *args: str) -> pd.DataFrame:
    '''Removes records with NaN in the specified column names from the dataframe.
    
    Args:
        df: The DataFrame to filter
        *args: Variable number of column names to filter

    Returns:
        A filtered copy of df
    '''

    df2 = df.copy()
    for arg in args:
        df2.dropna(subset = [arg], inplace=True)

    return df2