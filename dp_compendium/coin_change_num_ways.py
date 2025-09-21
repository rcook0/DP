"""
Coin Change (Number of Ways)
Order-insensitive unbounded coin change.
State:
  dp[a] = number of ways to make amount a
Recurrence:
  dp[a]+=dp[a-c] for each coin c
"""
def num_ways(coins, amount):
    dp = [0]*(amount+1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount+1):
            dp[a]+=dp[a-c]
    return dp[amount]

if __name__ == "__main__":
    print(num_ways([1,2,5], 5))  # 4
