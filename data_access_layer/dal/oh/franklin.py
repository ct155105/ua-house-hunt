import pandas as pd

def get_tax() -> pd.DataFrame:
    '''Loads and returns the tax accessor records
    
    Returns:
        A dataframe with all the tax records for the county
    '''
    
    df = pd.read_csv('data/oh/franklin/Parcel_Boundaries.csv')
    return df


def get_transactions() -> pd.DataFrame:
    '''Loads and returns the transcation records
    
    Returns:
        A dataframe with 3 years worth of transactions records for the county
    '''
    
    df = pd.read_csv('data/oh/franklin/Property_Sales_Transactions.csv', low_memory=False)
    return df


def get_combined(tax: pd.DataFrame = None, transactions: pd.DataFrame = None) -> pd.DataFrame:
    '''Inner joins the tax and assessor records. Can pass dataframes for tax and transactions if already loaded

    Args:
        tax (Optional): The dataframe containing the tax assessor records
        transactions (Optional): The dataframe containing the transactions records
    
    Returns:
        A DataFrame with the tax assessor's information appended to the transaction records
    '''
    
    if tax is None:
        tax = get_tax()

    if transactions is None:
        transactions = get_transactions()

    df =  pd.merge(transactions[["SalePrice",'SALEDATE','PARCELID']],tax,on='PARCELID')
    return df