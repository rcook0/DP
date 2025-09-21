def viterbi(states, start_p, trans_p, emit_p, obs):
    n=len(obs)
    m=len(states)
    import math
    def log(x): return -1e18 if x<=0 else math.log(x)
    dp=[[float('-inf')]*m for _ in range(n)]
    parent=[[-1]*m for _ in range(n)]
    for s in range(m):
        dp[0][s]=log(start_p[states[s]]) + log(emit_p[states[s]].get(obs[0], 0.0))
    for t in range(1,n):
        for s in range(m):
            best=float('-inf'); arg=-1
            for ps in range(m):
                val=dp[t-1][ps] + log(trans_p[states[ps]].get(states[s], 0.0)) + log(emit_p[states[s]].get(obs[t], 0.0))
                if val>best: best=val; arg=ps
            dp[t][s]=best; parent[t][s]=arg
    end=max(range(m), key=lambda s: dp[-1][s])
    path=[end]
    for t in range(n-1,0,-1):
        path.append(parent[t][path[-1]])
    path=list(reversed(path))
    return [states[i] for i in path]
