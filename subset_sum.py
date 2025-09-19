"""
Subset Sum (boolean)
State: dp[s] = True if sum s achievable
"""
def subset_sum(nums, target):
    dp = [False]*(target+1)
    dp[0] = True
    for x in nums:
        for s in range(target, x-1, -1):
            dp[s] = dp[s] or dp[s-x]
    return dp[target]

if __name__ == "__main__":
    print(subset_sum([3,34,4,12,5,2], 9))  # True
