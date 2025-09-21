"""
Floyd–Warshall with path reconstruction
"""
def floyd_warshall_with_path(dist):
    n=len(dist)
    nxt=[[None]*n for _ in range(n)]
    BIG=10**9
    for i in range(n):
        for j in range(n):
            if i!=j and dist[i][j]<BIG:
                nxt[i][j]=j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]+dist[k][j]<dist[i][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
                    nxt[i][j]=nxt[i][k]
    return dist, nxt

def reconstruct_path(nxt,u,v):
    if nxt[u][v] is None: return []
    path=[u]
    while u!=v:
        u=nxt[u][v]
        if u is None: return []
        path.append(u)
    return path

if __name__ == "__main__":
    INF=10**6
    dist=[[0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0]]
    D,nxt=floyd_warshall_with_path(dist)
    print(D[0][3], reconstruct_path(nxt,0,3))  # 6 [0,1,2,3]
