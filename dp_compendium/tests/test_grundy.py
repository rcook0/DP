import dp_compendium.grundy_subtraction as gs

def test_grundy():
    g=gs.grundy_numbers(10,[1,3,4])
    assert isinstance(g,list) and len(g)>=11
