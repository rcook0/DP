"""
Rod Cutting
State: dp[i] = max revenue for rod of length i
"""
def rod_cutting(prices, n):
    dp=[0]*(n+1)
    for i in range(1, n+1):
        best=0
        for cut in range(1, i+1):
            best=max(best, prices[cut-1]+dp[i-cut])
        dp[i]=best
    return dp[n]

if __name__ == "__main__":
    print(rod_cutting([1,5,8,9,10,17,17,20], 8))  # 22
