"""
0/1 Knapsack
State: dp[w] = max value for capacity w using processed items (1D optimized)
"""
def knapsack_01(values, weights, W):
    n = len(values)
    dp = [0]*(W+1)
    for i in range(n):
        v, w = values[i], weights[i]
        for cap in range(W, w-1, -1):
            dp[cap] = max(dp[cap], dp[cap-w] + v)
    return dp[W]

if __name__ == "__main__":
    print(knapsack_01([60,100,120],[10,20,30], 50))  # 220
