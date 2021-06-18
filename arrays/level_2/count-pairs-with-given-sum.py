# Q7, MEDIUM

def count_pairs_with_given_sum(arr, total):
    """Find number of pairs whose addition is equal to 'total'
    params:
    ---------------
    arr - array
    total - value to compare sum against

    returns:
    ---------------
    int, number of pairs satisfying above condition
    """
    n = len(arr)
    if n<2:
        raise Exception("At least 2 elements are required.")
    count_pair = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+arr[j])==total:
                count_pair+=1
        
    return count_pair


def count_pairs_fast(arr, total):
    """Find number of pairs whose addition is equal to 'total'
    params:
    ---------------
    arr - array
    total - value to compare sum against

    returns:
    ---------------
    int, number of pairs satisfying above condition
    """
    n = len(arr)
    if n<2:
        raise Exception("At least 2 elements are required.")
    count_pair = 0
    item_map = {}
    # create a map of item count
    for item in arr:
        item_map[item] = item_map[item] + 1 if item_map.get(item) else 1
    # check if the number can be combined with any other number
    # to produce total(except itself)
    for i in range(n):
        if (total-arr[i]) == arr[i]:
            count_pair -= 1
        if item_map.get(total-arr[i]):
            count_pair += item_map.get(total-arr[i])
    return count_pair//2



if __name__ == "__main__":
    print(count_pairs_with_given_sum([1,5,7,-1], 6))
    print(count_pairs_with_given_sum([1,5,7,-1], 4))
    print(count_pairs_with_given_sum([1,5,7,-1], 2))
    print(count_pairs_with_given_sum([5,-3,7,-1], 4))
    print(count_pairs_with_given_sum([1,-1,-1,-1], 0))
    print(count_pairs_with_given_sum([-1,-1,-1,-1], -2))

    print(count_pairs_fast([1,5,7,-1], 6))
    print(count_pairs_fast([1,5,7,-1], 4))
    print(count_pairs_fast([1,5,7,-1], 2))
    print(count_pairs_fast([5,-3,7,-1], 4))
    print(count_pairs_fast([1,-1,-1,-1], 0))
    print(count_pairs_fast([-1,-1,-1,-1], -2))

