"""
Matrix Chain Multiplication (Bottom-Up)
State: dp[i][j] = min cost for A_i..A_j, sizes encoded by p
"""
def matrix_chain_order(p):
    n = len(p)-1
    dp = [[0]*(n+1) for _ in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[1][n]

if __name__ == "__main__":
    p=[30,35,15,5,10,20,25]
    print(matrix_chain_order(p))  # 15125
