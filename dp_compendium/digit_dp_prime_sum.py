from functools import lru_cache
def _sieve(limit):
    is_p=[False,False]+[True]*(limit-1)
    for p in range(2,int(limit**0.5)+1):
        if is_p[p]:
            for q in range(p*p,limit+1,p): is_p[q]=False
    return is_p

def count_prime_digit_sum(N):
    digs=list(map(int,str(N))); n=len(digs)
    maxsum=9*n
    prime=_sieve(maxsum)
    @lru_cache(None)
    def dp(pos, tight, s):
        if pos==n: return 1 if prime[s] else 0
        limit=digs[pos] if tight else 9
        total=0
        for d in range(limit+1):
            total += dp(pos+1, tight and d==limit, s+d)
        return total
    return dp(0, True, 0)
