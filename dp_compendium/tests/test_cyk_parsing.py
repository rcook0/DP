import dp_compendium.cyk_parsing as cyk
def test_simple():
    prods={'S':[('S','S'),'A'], 'A':['a']}
    assert cyk.cyk_parse({'a'}, prods, 'S', 'aa') is True
