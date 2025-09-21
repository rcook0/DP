import heapq
def steiner_tree_cost(n, edges, terminals):
    g=[[] for _ in range(n)]
    for u,v,w in edges:
        g[u].append((v,w)); g[v].append((u,w))
    k=len(terminals)
    INF=10**15
    dp=[[INF]*n for _ in range(1<<k)]
    for i,t in enumerate(terminals):
        dp[1<<i][t]=0
    for mask in range(1, 1<<k):
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if other:
                for v in range(n):
                    nv = dp[sub][v] + dp[other][v]
                    if nv < dp[mask][v]:
                        dp[mask][v] = nv
            sub = (sub-1) & mask
        h=[]; dist=dp[mask][:]
        for v in range(n):
            if dist[v] < INF:
                heapq.heappush(h, (dist[v], v))
        while h:
            d,u = heapq.heappop(h)
            if d!=dist[u]: continue
            for w,c in g[u]:
                nd = d + c
                if nd < dist[w]:
                    dist[w]=nd
                    heapq.heappush(h,(nd,w))
        dp[mask]=dist
    full=(1<<k)-1
    return min(dp[full])
