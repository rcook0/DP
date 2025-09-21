"""
0/1 Knapsack
State:
  dp[w] = max value achievable with capacity w
Recurrence:
  dp[w] = max(dp[w], dp[w-wt[i]]+val[i]) iterating backwards
"""
def knapsack(values, weights, W):
    dp = [0]*(W+1)
    for v,w in zip(values, weights):
        for cap in range(W, w-1, -1):
            dp[cap] = max(dp[cap], dp[cap-w]+v)
    return dp[W]

if __name__ == "__main__":
    print(knapsack([60,100,120],[10,20,30],50))  # 220
