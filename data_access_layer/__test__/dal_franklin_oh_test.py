from dal.oh import franklin as dal


def test_get_tax():    
    tax = dal.get_tax()
    assert tax.shape[0] > 10000

    
def test_get_transactions():    
    transactions = dal.get_transactions()
    assert transactions.shape[0] > 10000


# def test_get_combined():
#     combined = dal.get_combined()
#     assert combined.shape[0] > 10000