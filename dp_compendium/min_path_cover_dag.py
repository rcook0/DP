def min_path_cover_by_matching(n, edges):
    g=[[] for _ in range(n)]
    for u,v in edges: g[u].append(v)
    matchR=[-1]*n
    def bpm(u, seen):
        for v in g[u]:
            if not seen[v]:
                seen[v]=True
                if matchR[v]==-1 or bpm(matchR[v], seen):
                    matchR[v]=u
                    return True
        return False
    match=0
    for u in range(n):
        seen=[False]*n
        if bpm(u, seen): match+=1
    return n - match
