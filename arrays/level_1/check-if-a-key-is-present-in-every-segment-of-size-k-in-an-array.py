# Q1, easy
def check_key_in_segment(arr, x, k):
    """Check if key x is present in each segment of size k in the array arr.
    params:
    -------------------
    arr - array
    x - key
    k - size of segment
    returns:
    -------------------
    bool, "Yes" if True. "No" if False.
    """
    n = len(arr)
    if k==0 or n==0:
        return "Both the segment size and array size should be greater than 0"
    if k>n:
        return f"Wrong Input....segment size is {k} which is more than {n}, the size of the array."
    flag = False
    segment_count = 0
    for i in range(n):
        if segment_count==k and flag:
            segment_count=0
            flag = False
        elif segment_count==k and not flag:
            return "No"
        if not flag and arr[i]==x:
            flag=True

        segment_count += 1
    if segment_count==k and not flag:
        return "No"
    return "Yes"

if __name__ == "__main__":
    print(check_key_in_segment(arr=[3,5,2,4,9,3,1,7,3,11,12,3], x=3, k=3))
    print(check_key_in_segment(arr=[1,2,3,4,5,6,7,8,9,10], x=2, k=5))
    print(check_key_in_segment(arr=[1], x=1, k=1))
    print(check_key_in_segment(arr=[1], x=1, k=2))
    print(check_key_in_segment(arr=[1,2,3,4,5], x=1, k=0))
