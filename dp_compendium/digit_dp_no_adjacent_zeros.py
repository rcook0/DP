from functools import lru_cache
def count_no_adjacent_zeros(N):
    digs=list(map(int,str(N))); n=len(digs)
    @lru_cache(None)
    def dp(pos,tight,prev_zero,started):
        if pos==n: return 1
        limit=digs[pos] if tight else 9
        tot=0
        for d in range(limit+1):
            ns = started or d!=0
            if ns and prev_zero and d==0: 
                continue
            tot += dp(pos+1, tight and d==limit, ns and d==0, ns)
        return tot
    return dp(0, True, False, False)
