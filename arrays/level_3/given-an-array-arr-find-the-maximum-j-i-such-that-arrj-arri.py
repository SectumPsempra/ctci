# Q5, Hard

def find_max_sum_difference(arr):
    """Given an array arr, find the maximum j-i where j and i are two indexes
    of the array arr such that arr[j] > arr[i].
    params:
    ---------------
    arr: array
    
    returns:
    ---------------
    number, max(j-i), where i != j
    """
    n = len(arr)
    store = -1234232123
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i] and (j-i)>store:
                store = j-i
    return store

def find_max_sum_diff(arr):
    # two pointer method
    n = len(arr)
    if n<2:
        return "minimum 2 elements required"
    i, j = 0, n-1
    first, last = arr[0], arr[-1]
    for index in range(n):
        if arr[j]>arr[i]:
            return j-i
        else:
            j-=1
    return -1

if __name__=="__main__":
    print(find_max_sum_difference([6,4,8,9,5,-1]))
    print(find_max_sum_difference([34,8,10,3,2,80,30,33,1]))
    print(find_max_sum_difference([9, 2, 3, 4, 5, 6, 7, 8, 18, 0]))
    print(find_max_sum_difference([1, 2, 3, 4, 5, 6]))
    print(find_max_sum_difference([6, 5, 4, 3, 2, 1]))

    print(find_max_sum_diff([6,4,8,9,5,-1]))
    print(find_max_sum_diff([34,8,10,3,2,80,30,33,1]))
    print(find_max_sum_diff([9, 2, 3, 4, 5, 6, 7, 8, 18, 0]))
    print(find_max_sum_diff([1, 2, 3, 4, 5, 6]))
    print(find_max_sum_diff([6, 5, 4, 3, 2, 1]))
