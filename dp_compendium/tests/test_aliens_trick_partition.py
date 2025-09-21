import dp_compendium.aliens_trick_partition as atp
def test_basic():
    assert atp.minimize_largest_sum([7,2,5,10,8], 2) == 18
