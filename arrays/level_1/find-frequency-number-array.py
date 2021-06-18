# Q9, EASY

def find_frequency(arr, x):
    """find frequency of a given number x in array arr
    params:
    ----------
    arr: array
    x: int, number whose frequency needs to be calculated

    returns:
    ----------
    int, frequency of x, 0 if x not found.
    """
    if not arr:
        return -1
    freq = 0
    for item in arr:
        if item==x:
            freq+=1
    return freq

if __name__ == "__main__":
    print(find_frequency([0,5,5,5,4], 5))
    print(find_frequency([1,2,3], 4))
    print(find_frequency([], 3))
