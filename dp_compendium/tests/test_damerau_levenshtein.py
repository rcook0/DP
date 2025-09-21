import dp_compendium.damerau_levenshtein as dl
def test_basic():
    assert dl.damerau_levenshtein('CA','AC') == 1
