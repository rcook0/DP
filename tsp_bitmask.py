"""
Traveling Salesman Problem (Bitmask DP), starting at 0
State: dp[mask][i] = min cost to reach i having visited 'mask'
"""
def tsp(dist):
    n=len(dist)
    INF=10**15
    dp=[[INF]*n for _ in range(1<<n)]
    dp[1][0]=0
    for mask in range(1<<n):
        for u in range(n):
            if not (mask & (1<<u)): continue
            cur = dp[mask][u]
            if cur>=INF: continue
            for v in range(n):
                if mask & (1<<v): continue
                nm = mask | (1<<v)
                dp[nm][v] = min(dp[nm][v], cur + dist[u][v])
    full = (1<<n)-1
    return min(dp[full][i] + dist[i][0] for i in range(n))

if __name__ == "__main__":
    dist=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    print(tsp(dist))  # 80
