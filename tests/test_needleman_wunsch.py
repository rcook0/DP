from sequence_alignment_traceback import needleman_wunsch_align

def test_nw_traceback():
    score, a_aln, b_aln = needleman_wunsch_align("GATTACA","GCATGCU", match=1, mismatch=-1, gap=-2)
    # known optimal score for these parameters
    assert isinstance(score, int)
    assert len(a_aln) == len(b_aln)
    # very light sanity checks
    assert '-' in a_aln or '-' in b_aln
