"""
Palindrome Partitioning (Minimum Cuts)
State: dp[i] = min cuts for s[:i+1]
"""
def min_cut_palindrome(s):
    n = len(s)
    dp = [0]*n
    pal = [[False]*n for _ in range(n)]
    for i in range(n):
        best = i
        for j in range(i+1):
            if s[j]==s[i] and (i-j<=1 or pal[j+1][i-1]):
                pal[j][i]=True
                best = 0 if j==0 else min(best, dp[j-1]+1)
        dp[i]=best
    return dp[-1]

if __name__ == "__main__":
    print(min_cut_palindrome("aab"))  # 1
