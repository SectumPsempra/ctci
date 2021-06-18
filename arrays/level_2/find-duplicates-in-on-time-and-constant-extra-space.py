# Q-11, MEDIUM

def find_duplicates(arr):
    """Print duplicate elements in array arr which is in range 0 to n-1, where n
    is the length of the array
    params:
    ----------------
    arr: array

    returns:
    ----------------
    None, print duplicates to console
    """
    n = len(arr)
    if n<2:
        print("No duplicates")
    else:
        for i in range(n):
            if arr[abs(arr[i])] > 0:
                arr[abs(arr[i])] *= -1
            else:
                print(abs(arr[i]),end=" ")

if __name__=="__main__":
    find_duplicates([1,2,3,6,3,6,1])
    print("\n") 
