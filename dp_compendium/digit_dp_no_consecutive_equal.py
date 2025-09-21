"""
Digit DP: count numbers up to N with no consecutive equal digits
"""
from functools import lru_cache
def count_no_repeat(N):
    digs=list(map(int,str(N))); n=len(digs)
    @lru_cache(None)
    def dp(pos,tight,prev):
        if pos==n: return 1
        limit=digs[pos] if tight else 9
        ans=0
        for d in range(0,limit+1):
            if d==prev: continue
            ans+=dp(pos+1, tight and d==limit, d)
        return ans
    return dp(0,True,-1)

if __name__ == "__main__":
    print(count_no_repeat(1000))
