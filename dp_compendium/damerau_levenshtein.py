def damerau_levenshtein(a,b):
    n,m=len(a),len(b)
    INF=n+m
    dp=[[0]*(m+2) for _ in range(n+2)]
    da={}
    dp[0][0]=INF
    for i in range(n+1):
        dp[i+1][0]=INF; dp[i+1][1]=i
    for j in range(m+1):
        dp[0][j+1]=INF; dp[1][j+1]=j
    for i in range(1,n+1):
        db=0
        for j in range(1,m+1):
            i1=da.get(b[j-1],0)
            j1=db
            cost = 0 if a[i-1]==b[j-1] else 1
            if cost==0: db=j
            dp[i+1][j+1] = min(
                dp[i][j] + cost,
                dp[i+1][j] + 1,
                dp[i][j+1] + 1,
                dp[i1][j1] + (i-i1-1) + 1 + (j-j1-1)
            )
        da[a[i-1]]=i
    return dp[n+1][m+1]
