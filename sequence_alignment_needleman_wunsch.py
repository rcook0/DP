"""
Global sequence alignment (Needleman–Wunsch)
State: dp[i][j] over prefixes with match/mismatch/gap scores
"""
def needleman_wunsch(a,b,match=1,mismatch=-1,gap=-2):
    n,m=len(a),len(b)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1): dp[i][0]=i*gap
    for j in range(1,m+1): dp[0][j]=j*gap
    for i in range(1,n+1):
        for j in range(1,m+1):
            score = match if a[i-1]==b[j-1] else mismatch
            dp[i][j] = max(dp[i-1][j-1]+score, dp[i-1][j]+gap, dp[i][j-1]+gap)
    return dp[n][m]

if __name__ == "__main__":
    print(needleman_wunsch("GATTACA","GCATGCU"))
