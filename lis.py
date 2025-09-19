"""
Longest Increasing Subsequence (O(n log n) patience sorting)
dp tails: tails[k] = smallest possible tail of an increasing subsequence of length k+1
"""
import bisect

def lis_length(arr):
    tails = []
    for x in arr:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

if __name__ == "__main__":
    print(lis_length([10,9,2,5,3,7,101,18]))  # 4
