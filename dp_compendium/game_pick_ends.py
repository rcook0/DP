def optimal_first_player_score(arr):
    n=len(arr)
    dp=[[0]*n for _ in range(n)]
    for i in range(n): dp[i][i]=arr[i]
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            pick_left = arr[i] + min(dp[i+2][j] if i+2<=j else 0, dp[i+1][j-1] if i+1<=j-1 else 0)
            pick_right= arr[j] + min(dp[i+1][j-1] if i+1<=j-1 else 0, dp[i][j-2] if i<=j-2 else 0)
            dp[i][j]=max(pick_left, pick_right)
    return dp[0][n-1]
