"""
Longest Increasing Subsequence (LIS)
Patience sorting method, O(n log n).
"""
import bisect
def lis_length(arr):
    tails=[]
    for x in arr:
        i=bisect.bisect_left(tails,x)
        if i==len(tails): tails.append(x)
        else: tails[i]=x
    return len(tails)

if __name__ == "__main__":
    print(lis_length([10,9,2,5,3,7,101,18]))  # 4
