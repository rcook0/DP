"""
House Robber
State: dp[i] = max sum up to i without robbing adjacent houses
"""
def house_robber(nums):
    prev2=0; prev1=0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2+x)
    return prev1

if __name__ == "__main__":
    print(house_robber([2,7,9,3,1]))  # 12
