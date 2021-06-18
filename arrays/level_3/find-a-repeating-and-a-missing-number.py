# Q8, HARD

def find_missing_and_repeating(arr):
    """find missing and repeating number in array arr which is in
    range 1 to n.
    params:
    -------------------------------
    arr: array

    returns:
    ------------------------------
    int, int: missing number, repeating number
    """
    n = len(arr)
    if n<2:
        return "At least 2 numbers required in array"
    else:
        count_dict = {}
        missing_number, repeating_number = None, None
        for item in arr:
            if count_dict.get(item):
                repeating_number = item
                count_dict[item]+=1
            else:
                count_dict[item]=1
        for i in range(1,n+1):
            if not count_dict.get(i):
                missing_number = i
        return f"missing number is: {missing_number}, repeating number is: {repeating_number}"


if __name__ == "__main__":
    print(find_missing_and_repeating([1,2,2]))
    print(find_missing_and_repeating([2]))
    print(find_missing_and_repeating([1,3,4,2,2]))
