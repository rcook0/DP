def knuth_opt_slimes(weights):
    n=len(weights)
    pref=[0]
    for w in weights: pref.append(pref[-1]+w)
    def sumij(i,j): return pref[j]-pref[i]
    INF=10**18
    dp=[[0]*(n+1) for _ in range(n+1)]
    opt=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n): dp[i][i+1]=0; opt[i][i+1]=i+1
    for L in range(2,n+1):
        for i in range(0, n-L+1):
            j=i+L
            dp[i][j]=INF
            start=opt[i][j-1] if opt[i][j-1] else i+1
            end=opt[i+1][j] if opt[i+1][j] else j-1
            for k in range(start-1, end):
                val=dp[i][k+1]+dp[k+1][j]+sumij(i,j)
                if val<dp[i][j]:
                    dp[i][j]=val; opt[i][j]=k+1
    return dp[0][n]

def dc_opt_dp(cost, n, K):
    INF=10**18
    prev=[0]+[INF]*n
    for _ in range(1,K+1):
        cur=[0]+[INF]*n
        def solve(l,r,optl,optr):
            if l>r: return
            mid=(l+r)//2
            best=(INF,-1)
            start=optl; end=min(mid-1, optr)
            for k in range(start, end+1):
                cand=prev[k]+cost(k,mid)
                if cand<best[0]:
                    best=(cand,k)
            cur[mid]=best[0]
            arg=best[1]
            solve(l, mid-1, optl, arg)
            solve(mid+1, r, arg, optr)
        solve(1,n,0,n-1)
        prev=cur
    return prev[n]
