import dp_compendium.mdp_value_iteration as mdp

def test_runs():
    S=['A','B','C']
    A={'A':['stay','go'],'B':['stay','go'],'C':['stay']}
    def P(s,a):
        if s=='A' and a=='go': return [(0.7,'B'),(0.3,'C')]
        if s=='B' and a=='go': return [(0.6,'C'),(0.4,'A')]
        return [(1.0,s)]
    def R(s,a,sp):
        return 1.0 if sp=='C' else 0.0
    V,pi=mdp.value_iteration(S,A,P,R,0.9)
    assert set(V.keys())==set(S)
