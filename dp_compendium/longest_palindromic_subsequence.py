"""
Longest Palindromic Subsequence (LPS)
State: dp[i][j] = LPS length of s[i..j]
"""
def lps(s):
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for i in range(n): dp[i][i]=1
    for L in range(2, n+1):
        for i in range(n-L+1):
            j=i+L-1
            if s[i]==s[j]:
                dp[i][j]=2 if L==2 else dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

if __name__ == "__main__":
    print(lps("bbbab"))  # 4
