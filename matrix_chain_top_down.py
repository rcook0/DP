"""
Matrix Chain Multiplication (Top-Down + Memoization)
"""
from functools import lru_cache

def matrix_chain_order_topdown(p):
    n = len(p)-1
    @lru_cache(None)
    def dp(i,j):
        if i==j: return 0
        best = float('inf')
        for k in range(i, j):
            best = min(best, dp(i,k) + dp(k+1,j) + p[i-1]*p[k]*p[j])
        return best
    return dp(1, n)

if __name__ == "__main__":
    p=[30,35,15,5,10,20,25]
    print(matrix_chain_order_topdown(p))  # 15125
