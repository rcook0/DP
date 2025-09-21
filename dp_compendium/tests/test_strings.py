import dp_compendium.lis as lis
import dp_compendium.lcs_traceback as lcs
import dp_compendium.edit_distance as ed
import dp_compendium.longest_palindromic_subsequence as lps
import dp_compendium.palindrome_partitioning_min_cuts as ppc

def test_lis():
    assert lis.lis_length([10,9,2,5,3,7,101,18]) == 4

def test_lcs():
    length, subseq = lcs.lcs_with_trace("ABCBDAB","BDCABA")
    assert length == 4
    assert set(subseq).issubset(set("ABCBD"))

def test_edit_distance():
    assert ed.edit_distance("kitten","sitting") == 3

def test_lps():
    assert lps.lps("bbbab") == 4

def test_pal_partition():
    assert ppc.min_cut_pal("aab") == 1
