import dp_compendium.tree_max_independent_set as mis
import dp_compendium.egg_dropping as egg
import dp_compendium.painters_partition as pp

def test_tree_mis():
    assert mis.tree_mis(6,[(0,1),(0,2),(1,3),(1,4),(2,5)]) >= 3

def test_egg_drop():
    assert egg.egg_drop(2,10) > 0

def test_painters_partition():
    assert pp.painters_partition([10,20,30,40],2)==60
