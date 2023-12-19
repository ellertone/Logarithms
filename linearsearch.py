def linear_search(list, target):
    """
    Returns index psition
    """
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target is found at index ", index  )
    else:
        print("Target not found in list")

numbers = [1,2,4,6,7,8,5,8,5,8,6]

result = linear_search(numbers,12)
verify(result)