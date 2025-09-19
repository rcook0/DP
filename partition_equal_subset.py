"""
Partition Equal Subset Sum
Reduce to subset sum with target total//2
"""
def can_partition(nums):
    total = sum(nums)
    if total % 2: return False
    target = total//2
    dp = [False]*(target+1)
    dp[0] = True
    for x in nums:
        for s in range(target, x-1, -1):
            dp[s] = dp[s] or dp[s-x]
    return dp[target]

if __name__ == "__main__":
    print(can_partition([1,5,11,5]))  # True
