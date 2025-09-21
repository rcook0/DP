import dp_compendium.coin_change_min_coins as ccmc
import dp_compendium.coin_change_num_ways as ccw

def test_min_coins_basic():
    assert ccmc.min_coins([1,3,4], 6) == 2
    assert ccmc.min_coins([2], 3) == -1

def test_num_ways_basic():
    assert ccw.num_ways([1,2,5], 5) == 4
    assert ccw.num_ways([2], 3) == 0
