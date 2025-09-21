from functools import lru_cache
def count_sum_divisible_by_k(N, K):
    digs=list(map(int,str(N))); n=len(digs)
    @lru_cache(None)
    def dp(pos,tight,mod):
        if pos==n: return 1 if mod%K==0 else 0
        limit=digs[pos] if tight else 9
        tot=0
        for d in range(limit+1):
            tot+=dp(pos+1, tight and d==limit, (mod+d)%K)
        return tot
    return dp(0,True,0)
