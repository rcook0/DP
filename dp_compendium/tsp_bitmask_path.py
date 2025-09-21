"""
Traveling Salesman Problem (TSP) with bitmask DP and path reconstruction.
"""
def tsp_with_path(dist):
    n=len(dist); INF=10**15
    dp=[[INF]*n for _ in range(1<<n)]
    parent=[[ -1]*n for _ in range(1<<n)]
    dp[1][0]=0
    for mask in range(1<<n):
        for u in range(n):
            if not (mask&(1<<u)): continue
            cur=dp[mask][u]
            if cur>=INF: continue
            for v in range(n):
                if mask&(1<<v): continue
                nm=mask|(1<<v); cand=cur+dist[u][v]
                if cand<dp[nm][v]:
                    dp[nm][v]=cand; parent[nm][v]=u
    full=(1<<n)-1
    best,end=min((dp[full][i]+dist[i][0],i) for i in range(n))
    tour=[0]*n; mask=full; u=end
    for idx in range(n-1,-1,-1):
        tour[idx]=u; pu=parent[mask][u]
        if pu==-1 and idx!=0: break
        mask^=(1<<u); u=pu
    tour.append(0)
    return best, tour

if __name__ == "__main__":
    dist=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    cost,tour=tsp_with_path(dist)
    print(cost,tour)
