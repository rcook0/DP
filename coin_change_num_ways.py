"""
Coin Change (Number of Ways) — Unbounded order-insensitive
State: dp[a] = number of ways to make amount a using processed coins
Order coins outer loop to avoid permutations.
Time: O(amount * n_coins)
"""
def num_ways(coins, amount):
    dp = [0]*(amount+1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount+1):
            dp[a] += dp[a-c]
    return dp[amount]

if __name__ == "__main__":
    print(num_ways([1,2,5], 5))  # 4
