import dp_compendium.min_path_cover_dag as mpc

def test_line():
    n=4; edges=[(0,1),(1,2),(2,3)]
    assert mpc.min_path_cover_by_matching(n, edges) == 1
