from ct_math import algebra as a

def test_get_average_of_list_values():
    list = [0,1,2]
    mean = a.get_average_of_list_values(list)

    assert mean == 1

    list = [1,2]
    mean = a.get_average_of_list_values(list)

    assert mean == 1.5