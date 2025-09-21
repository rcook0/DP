def value_iteration(S,A,P,R,gamma=0.95,eps=1e-6,max_iter=10000):
    V={s:0.0 for s in S}
    for _ in range(max_iter):
        delta=0.0
        Vnew={}
        for s in S:
            best=-1e18; best_a=None
            for a in A[s]:
                exp=0.0
                for p,sp in P(s,a):
                    exp += p*(R(s,a,sp) + gamma*V[sp])
                if exp>best:
                    best=exp; best_a=a
            Vnew[s]=best
            delta=max(delta, abs(Vnew[s]-V[s]))
        V=Vnew
        if delta<eps: break
    pi={}
    for s in S:
        best=-1e18; best_a=None
        for a in A[s]:
            exp=0.0
            for p,sp in P(s,a):
                exp += p*(R(s,a,sp) + gamma*V[sp])
            if exp>best: best=exp; best_a=a
        pi[s]=best_a
    return V, pi
