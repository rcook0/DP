from floyd_warshall_paths import floyd_warshall_with_path, reconstruct_path

def test_fw_paths():
    INF = 10**9
    dist = [
        [0,3,INF,7],
        [8,0,2,INF],
        [5,INF,0,1],
        [2,INF,INF,0],
    ]
    D, nxt = floyd_warshall_with_path(dist)
    path = reconstruct_path(nxt, 0, 3)
    # Shortest path 0->1->2->3 with cost 3+2+1=6 is better than direct 7
    assert path in ([0,1,2,3],)  # simple sanity
    assert D[0][3] == 6
