"""
Edit Distance (Levenshtein)
State: dp[i][j] = min edits to transform a[:i] -> b[:j]
Transition: insert/delete/replace
"""
def edit_distance(a,b):
    n,m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][0] = i
    for j in range(m+1): dp[0][j] = j
    for i in range(1,n+1):
        for j in range(1,m+1):
            cost = 0 if a[i-1]==b[j-1] else 1
            dp[i][j] = min(
                dp[i-1][j] + 1,      # delete
                dp[i][j-1] + 1,      # insert
                dp[i-1][j-1] + cost  # replace
            )
    return dp[n][m]

if __name__ == "__main__":
    print(edit_distance("kitten","sitting"))  # 3
