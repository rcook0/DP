from coin_change_min_coins import min_coins
from coin_change_num_ways import num_ways

def test_coin_change():
    assert min_coins([1,3,4], 6) == 2
    assert num_ways([1,2,5], 5) == 4
