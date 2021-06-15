# Q3, Easy

def find_max(arr):
    """Find maximum element of given array arr
    params:
    ---------------
    arr: input array
    
    returns:
    ---------------
    number if arr.len>1
    """
    n = len(arr)
    if n==0:
        return "array should have at least one element"
    elif n==1:
        return arr[0]
    else:
        curr_max = arr[0]
        for i in range(1, n):
            if arr[i]>curr_max:
                curr_max=arr[i]
        return curr_max

def find_min(arr):
    """Find minimum element of given array arr
    params:
    ---------------
    arr: input array
    
    returns:
    ---------------
    number if arr.len>1
    """
    n = len(arr)
    if n==0:
        return "array should have at least one element"
    elif n==1:
        return arr[0]
    else:
        curr_min = arr[0]
        for i in range(1, n):
            if arr[i]<curr_min:
                curr_min=arr[i]
        return curr_min

if __name__ == "__main__":
    print(find_max([1,2,3]))
    print(find_max([1,2]))
    print(find_max([1]))
    print(find_max([]))

    print(find_min([1,2,3]))
    print(find_min([1,2]))
    print(find_min([1]))
    print(find_min([]))

