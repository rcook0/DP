"""
Digit DP: count numbers in [0..N] with no consecutive equal digits
State: dp[pos][tight][prev_digit]
"""
from functools import lru_cache

def count_no_repeat(N:int):
    digits = list(map(int, str(N)))
    n=len(digits)
    @lru_cache(None)
    def dp(pos, tight, prev):
        if pos==n: return 1
        limit = digits[pos] if tight else 9
        ans = 0
        for d in range(0, limit+1):
            if d == prev: 
                continue
            ans += dp(pos+1, tight and d==limit, d)
        return ans
    return dp(0, True, -1)

if __name__ == "__main__":
    print(count_no_repeat(1000))
