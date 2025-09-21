import dp_compendium.matrix_chain_reconstruct as mc
import dp_compendium.optimal_bst as obst
import dp_compendium.polygon_triangulation as tri

def test_matrix_chain():
    cost,parens=mc.matrix_chain_parenthesize([30,35,15,5,10,20,25])
    assert cost==15125

def test_optimal_bst():
    cost=obst.optimal_bst([34,8,50])
    assert cost>0

def test_triangulation():
    cost=tri.triangulation([(0,0),(2,0),(3,1),(2,2),(0,2)])
    assert cost>0
