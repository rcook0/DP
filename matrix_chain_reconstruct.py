"""
Matrix Chain Multiplication with optimal parenthesization reconstruction.

State:
  dp[i][j] = min cost to multiply A_i..A_j
  split[i][j] = k that achieves the minimum

Returns:
  (cost, parenthesization_string)
"""
def matrix_chain_parenthesize(p):
    n = len(p) - 1
    dp = [[0]*(n+1) for _ in range(n+1)]
    split = [[0]*(n+1) for _ in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    def build(i,j):
        if i == j: return f"A{i}"
        k = split[i][j]
        return f"({build(i,k)}{build(k+1,j)})"
    return dp[1][n], build(1, n)

if __name__ == "__main__":
    p=[30,35,15,5,10,20,25]
    cost, parens = matrix_chain_parenthesize(p)
    print(cost)
    print(parens)
