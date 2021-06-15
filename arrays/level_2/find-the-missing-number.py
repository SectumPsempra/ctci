# Q4, Medium

def _find_missing_using_summation(arr):
    n = len(arr) + 1
    return sum(range(1,n+1)) - sum(arr)

def _find_missing_using_bitwise(arr):
    # implemented after looking at the solution
    n = len(arr) + 1
    xor_arr = arr[0]
    for i in range(1,n-1):
        xor_arr = xor_arr ^ arr[i]
    xor_n = 1
    for i in range(2,n+1):
        xor_n = xor_n ^ i

    return xor_arr^xor_n

def find_missing_number(arr, method="summation"):
    """Given an array arr having elements from 1...n consecutive elements
    find the missing number.
    params
    ----------------
    arr: array
    method: method to find missing number
    
    returns
    ----------------
    number: missing number
    """

    if not arr:
        return "minimum one element expected"

    if method=="summation":
        return _find_missing_using_summation(arr)
    elif method=="bitwise":
        return _find_missing_using_bitwise(arr)
    else:
        return -1

if __name__ == "__main__":
    print(find_missing_number([1,2,4]))
    print(find_missing_number([1,2,4], "bitwise"))
    print(find_missing_number([1,2]))
    print(find_missing_number([2]))
    print(find_missing_number([2], "bitwise"))
