from matrix_chain_reconstruct import matrix_chain_parenthesize

def test_mcm_cost():
    p=[30,35,15,5,10,20,25]
    cost, parens = matrix_chain_parenthesize(p)
    assert cost == 15125
    # Parenthesization string shape sanity:
    assert parens.count('A') == 6
    assert parens[0]=='(' and parens[-1]==')'
