import dp_compendium.wildcard_match as wm
import dp_compendium.regex_match as rm
import dp_compendium.shortest_common_superseq as scs
import dp_compendium.distinct_subseq_count as dsc
import dp_compendium.min_window_subseq as mws

def test_wildcard():
    assert wm.is_match('adceb','*a*b') is True
    assert wm.is_match('acdcb','a*c?b') is False

def test_regex():
    assert rm.is_regex_match('aab','c*a*b') is True

def test_scs():
    assert scs.scs('abac','cab') == 5

def test_distinct():
    assert dsc.num_distinct('rabbbit','rabbit') == 3

def test_min_window():
    assert mws.min_window_subseq('abcdebdde','bde') == 'bcde'
