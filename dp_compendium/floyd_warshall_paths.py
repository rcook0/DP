def floyd_warshall_with_path(dist):
    n = len(dist)
    nxt = [[None]*n for _ in range(n)]
    BIG = 10**18
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] < BIG:
                nxt[i][j] = j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
    return dist, nxt

def reconstruct_path(nxt, u, v):
    if nxt[u][v] is None: return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        if u is None: return []
        path.append(u)
    return path
