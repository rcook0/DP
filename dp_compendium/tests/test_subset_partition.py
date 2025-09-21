import dp_compendium.subset_sum as ss
import dp_compendium.partition_equal_subset as pes

def test_subset_sum():
    assert ss.subset_sum([3,34,4,12,5,2], 9) == True
    assert ss.subset_sum([3,34,4,12,5,2], 30) == False

def test_partition_equal_subset():
    assert pes.can_partition([1,5,11,5]) == True
    assert pes.can_partition([1,2,3,5]) == False
