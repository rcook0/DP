import dp_compendium.hamiltonian_count as hc

def test_triangle():
    adj=[[0,1,1],[1,0,1],[1,1,0]]
    assert hc.count_hamiltonian_cycles(adj) == 1
