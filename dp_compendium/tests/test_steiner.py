import dp_compendium.steiner_tree_bitmask as st

def test_steiner():
    n=4
    edges=[(0,1,1),(1,2,1),(2,3,1),(3,0,1),(0,2,2),(1,3,2)]
    assert st.steiner_tree_cost(n, edges, [0,2]) == 2
