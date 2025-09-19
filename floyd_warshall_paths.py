"""
Floyd–Warshall with path reconstruction via successor matrix.

Input:
  dist: adjacency matrix (use large INF for no edge). Modified in-place.

Output:
  (D, nxt) where D is distance matrix, nxt[u][v] is the next node from u on the shortest path to v.
"""
def floyd_warshall_with_path(dist):
    n = len(dist)
    # initialize successor matrix
    nxt = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] < 10**18:
                nxt[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]

    return dist, nxt

def reconstruct_path(nxt, u, v):
    if nxt[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        if u is None:
            return []
        path.append(u)
    return path

if __name__ == "__main__":
    INF = 10**9
    dist = [
        [0,3,INF,7],
        [8,0,2,INF],
        [5,INF,0,1],
        [2,INF,INF,0],
    ]
    D, nxt = floyd_warshall_with_path(dist)
    print(D)
    print(reconstruct_path(nxt, 0, 3))
