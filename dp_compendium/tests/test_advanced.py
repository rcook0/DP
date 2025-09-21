import dp_compendium.digit_dp_no_consecutive_equal as ddp
import dp_compendium.sequence_alignment_traceback as sa
import dp_compendium.dtw as dtw

def test_digit_dp():
    assert ddp.count_no_repeat(100) > 0

def test_alignment():
    score,a_aln,b_aln=sa.needleman_wunsch_align("GATTACA","GCATGCU")[:3]
    assert isinstance(score,int)
    assert len(a_aln)==len(b_aln)

def test_dtw():
    dist=dtw.dtw([1,2,3],[2,2,3])
    assert dist>=0
