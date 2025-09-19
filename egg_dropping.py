"""
Egg Dropping (classic DP)
State: dp[e][f] = min worst-case drops with e eggs and f floors
"""
def egg_drop(e, f):
    dp=[[0]*(f+1) for _ in range(e+1)]
    for j in range(1, f+1): dp[1][j]=j
    for i in range(2, e+1):
        for j in range(1, f+1):
            best = 10**9
            for x in range(1, j+1):
                worst = 1 + max(dp[i-1][x-1], dp[i][j-x])
                if worst < best: best = worst
            dp[i][j]=best
    return dp[e][f]

if __name__ == "__main__":
    print(egg_drop(2, 10))  # 4
