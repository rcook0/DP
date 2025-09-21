import dp_compendium.partition_numbers as pn
def test_small():
    assert pn.stirling2(5,2) == 15
    assert pn.bell(5) == 52
