"""
Unbounded Knapsack
State:
  dp[w] = max value achievable with capacity w
Recurrence:
  dp[cap] = max(dp[cap], dp[cap-w[i]]+val[i]) for all items
"""
def knapsack_unbounded(values, weights, W):
    dp = [0]*(W+1)
    for cap in range(W+1):
        for v,w in zip(values, weights):
            if w<=cap:
                dp[cap] = max(dp[cap], dp[cap-w]+v)
    return dp[W]

if __name__ == "__main__":
    print(knapsack_unbounded([10,30,20],[5,10,15],60))
