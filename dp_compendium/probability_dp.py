def prob_heads_before_tails(H,T):
    dp=[[0.0]*T for _ in range(H)]
    for h in range(H):
        for t in range(T):
            if h==H-1: dp[h][t]=1.0
            elif t==T-1: dp[h][t]=0.0
            else:
                dp[h][t]=0.5*dp[h+1][t] + 0.5*dp[h][t+1]
    return dp[0][0]

def dice_ways(k,target):
    dp=[[0]*(target+1) for _ in range(k+1)]
    dp[0][0]=1
    for i in range(1,k+1):
        for s in range(1, target+1):
            acc=0
            for d in range(1,7):
                if s-d>=0: acc+=dp[i-1][s-d]
            dp[i][s]=acc
    return dp[k][target]
