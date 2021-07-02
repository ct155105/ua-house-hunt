
def get_average_of_list_values(list: list) -> float:
    '''Sums the values in the list, then divides by the list length
    
    Args:
        list: A list containing number values

    Returns
        the mean for the values in the list
    '''

    total = 0
    for val in list:
        total += val
    
    mean = total / len(list)

    return mean
