def linear_search(list, target):
    """
    Returns index psition
    """
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i