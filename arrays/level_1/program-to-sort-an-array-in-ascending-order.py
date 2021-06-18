# Q6, EASY

def selection_sort(arr):
    """sort given array in ascending order using selection sort
    params:
    ----------------------
    arr: input array

    returns:
    ----------------------
    sorted array in ascending order
    """
    n = len(arr)
    if n<2:
        print("need more than one element to sort.")
        pass
    else:
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if arr[j]<arr[min_idx]:
                    min_idx=j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    """sort given array arr in ascending order using bubble sort
    params:
    ----------------------
    arr: input array
    
    returns:
    ----------------------
    sorted array in ascending order
    """
    n = len(arr)
    if n<2:
        print("need more than one element to sort.")
        pass
    else:
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    print(bubble_sort([5,2,4,3,-1,0,1]))
    print(bubble_sort([5,1,4,2,8]))
    print(bubble_sort([1]))
    print(bubble_sort([]))

    print(selection_sort([5,2,4,3,-1,0,1]))
    print(selection_sort([5,1,4,2,8]))
    print(selection_sort([1]))
    print(selection_sort([]))
    


