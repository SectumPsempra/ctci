# Q10, EASY

def sort_0_1_2(arr):
    """Sort array of 0s, 1s and 2s in ascending order
    params:
    ---------
    arr: input

    returns:
    ---------
    arr, sorted array in ascendin order
    """
    n = len(arr)
    if n<2:
        pass
    else:
        counter_0, counter_1 = 0, 0
        for item in arr:
            if item==0:
                counter_0+=1
            elif item==1:
                counter_1+=1
        for i in range(n):
            if i<counter_0:
                arr[i] = 0
            elif i>=counter_0 and i<(counter_0+counter_1):
                arr[i]=1
            else:
                arr[i]=2
    return arr


if __name__ == "__main__":
    print(sort_0_1_2([0,1,2,0,1,2]))
    print(sort_0_1_2([0,1,1,0,1,2,1,2,0,0,0,1]))
