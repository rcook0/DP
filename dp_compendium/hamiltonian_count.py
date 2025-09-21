def count_hamiltonian_cycles(adj):
    n=len(adj)
    if n==0: return 0
    dp=[[0]*n for _ in range(1<<n)]
    dp[1][0]=1
    for mask in range(1<<n):
        if not (mask & 1): continue
        for v in range(n):
            if not (mask & (1<<v)): continue
            ways = dp[mask][v]
            if ways==0: continue
            for u in range(n):
                if adj[v][u] and not (mask & (1<<u)):
                    dp[mask | (1<<u)][u] += ways
    full=(1<<n)-1
    cycles=0
    for v in range(1,n):
        if adj[v][0]:
            cycles += dp[full][v]
    return cycles//2
