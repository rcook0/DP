"""
Coin Change (Minimum Coins)
State: dp[a] = min coins to make amount a
Recurrence: dp[a] = min(dp[a], dp[a-c] + 1) for each coin c if a>=c
Time: O(amount * n_coins), Space: O(amount)
"""
def min_coins(coins, amount):
    INF = 10**15
    dp = [INF]*(amount+1)
    dp[0] = 0
    for a in range(1, amount+1):
        for c in coins:
            if a >= c:
                dp[a] = min(dp[a], dp[a-c] + 1)
    return -1 if dp[amount] >= 10**14 else dp[amount]

if __name__ == "__main__":
    print(min_coins([1,3,4], 6))  # 2
