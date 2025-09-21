def stirling2(n,k,mod=None):
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            val = j*dp[i-1][j] + dp[i-1][j-1]
            dp[i][j] = val%mod if mod else val
    return dp[n][k]

def bell(n,mod=None):
    B=[[0]*(n+1) for _ in range(n+1)]
    B[0][0]=1
    for i in range(1,n+1):
        B[i][0]=B[i-1][i-1]
        for j in range(1,i+1):
            v = B[i][j-1]+B[i-1][j-1]
            B[i][j] = v%mod if mod else v
    return B[n][0]
