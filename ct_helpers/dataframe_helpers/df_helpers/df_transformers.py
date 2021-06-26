import pandas as pd

def trim_col_names(df: pd.DataFrame) -> pd.DataFrame:
    '''Removes spaces from column names
    
        Args:
            df: The DataFrame whose columns will be trimmed

        Returns:
            The original dataframe with trimmed column names

    '''

    new_cols = {}
    for col in df.columns:
        new_cols[col] = col.replace(" ",'')
    renamed_df = df.rename(new_cols, axis=1)

    return renamed_df
        