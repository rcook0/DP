def lcs_with_trace(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j] if dp[i-1][j] >= dp[i][j-1] else dp[i][j-1]
    i, j = n, m
    out = []
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            out.append(a[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return dp[n][m], ''.join(reversed(out))

if __name__ == "__main__":
    print(lcs_with_trace("abcde","ace"))
