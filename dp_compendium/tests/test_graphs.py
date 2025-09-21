import dp_compendium.floyd_warshall_paths as fw
import dp_compendium.tsp_bitmask_path as tsp

def test_floyd_warshall():
    INF=10**6
    dist=[[0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0]]
    D,nxt=fw.floyd_warshall_with_path([row[:] for row in dist])
    path=fw.reconstruct_path(nxt,0,3)
    assert D[0][3]==6
    assert path[0]==0 and path[-1]==3

def test_tsp():
    dist=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    cost,tour=tsp.tsp_with_path(dist)
    assert cost==80
    assert tour[0]==0 and tour[-1]==0
