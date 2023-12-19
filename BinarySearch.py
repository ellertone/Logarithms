def binary_search(list,target):
    """
    Implementing binary search
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2 # floor rounds down
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

