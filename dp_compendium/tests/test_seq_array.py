import dp_compendium.max_sum_incr_subseq as msis
import dp_compendium.longest_bitonic_subseq as lbs
import dp_compendium.max_submatrix_sum as mss
import dp_compendium.partition_array_max_sum as pams

def test_msis():
    assert msis.max_sum_incr_subseq([1,101,2,3,100,4,5]) == 106

def test_bitonic():
    assert lbs.longest_bitonic_subseq([1,11,2,10,4,5,2,1]) == 6

def test_submatrix():
    mat=[[1,-2,-1,4],[-8,3,4,2],[3,8,10,-8],[-4,-1,1,7]]
    assert mss.max_submatrix_sum(mat) == 27

def test_partition():
    assert pams.partition_array_max_sum([1,15,7,9,2,5,10],3) == 84
