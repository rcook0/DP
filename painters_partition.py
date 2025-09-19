"""
Painter's Partition
State: dp[i][k] = min time to paint first i boards with k painters
"""
def painters_partition(arr, k):
    n=len(arr)
    pref=[0]
    for x in arr: pref.append(pref[-1]+x)
    def segsum(i,j): return pref[j]-pref[i]
    dp=[[0]*(k+1) for _ in range(n+1)]
    for i in range(1,n+1): dp[i][1]=pref[i]
    for p in range(2, k+1):
        for i in range(1, n+1):
            best=10**18
            for j in range(i):
                best=min(best, max(dp[j][p-1], segsum(j, i)))
            dp[i][p]=best
    return dp[n][k]

if __name__ == "__main__":
    print(painters_partition([10,20,30,40], 2))  # 60
