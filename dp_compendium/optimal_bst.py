"""
Optimal BST with frequencies
"""
def optimal_bst(freq):
    n=len(freq)
    dp=[[0]*n for _ in range(n)]
    pref=[0]
    for f in freq: pref.append(pref[-1]+f)
    def sumf(i,j): return pref[j+1]-pref[i]
    for L in range(1,n+1):
        for i in range(n-L+1):
            j=i+L-1; best=float('inf')
            for r in range(i,j+1):
                left=0 if r==i else dp[i][r-1]
                right=0 if r==j else dp[r+1][j]
                best=min(best,left+right+sumf(i,j))
            dp[i][j]=best
    return dp[0][n-1]

if __name__ == "__main__":
    print(optimal_bst([34,8,50]))
