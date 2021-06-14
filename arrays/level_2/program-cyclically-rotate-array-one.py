# Q2, Medium

def rotate_arr_by_one(arr):
    """Cyclically rotate given array arr by one position
    params:
    ----------
    arr: array
    returns:
    ----------
    rotated array by one position
    """
    n = len(arr)
    if n<2:
        return arr
    last_element = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_element
    return arr

if __name__ == "__main__":
    print(rotate_arr_by_one([1,2,3]))
    print(rotate_arr_by_one([1,2]))
    print(rotate_arr_by_one([1]))
    print(rotate_arr_by_one([]))
