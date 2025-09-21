import dp_compendium.affine_gap_alignment as aga
def test_runs():
    s = aga.needleman_wunsch_affine('GATTACA','GCATGCU')
    assert isinstance(s, int)
