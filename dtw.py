"""
Dynamic Time Warping (DTW) distance between two sequences
State: dp[i][j] aligns prefix i of a with prefix j of b
"""
def dtw(a, b):
    n,m=len(a),len(b)
    INF=10**18
    dp=[[INF]*(m+1) for _ in range(n+1)]
    dp[0][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            cost = abs(a[i-1]-b[j-1])
            dp[i][j] = cost + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

if __name__ == "__main__":
    print(dtw([1,2,3,3,2,0],[0,1,1,2,3,3]))
