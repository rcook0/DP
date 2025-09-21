import dp_compendium.dp_optimizations as opt
def test_knuth():
    assert opt.knuth_opt_slimes([3,2,4,1]) > 0
def test_dc_opt():
    arr=[3,1,4,1,5,9]; p=[0]
    for x in arr: p.append(p[-1]+x)
    C=lambda i,j: (p[j]-p[i])**2
    assert opt.dc_opt_dp(C, len(arr), 3) >= 0
