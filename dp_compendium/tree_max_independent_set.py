"""
Tree Maximum Independent Set
"""
from collections import defaultdict
def tree_mis(n, edges):
    g=defaultdict(list)
    for u,v in edges:
        g[u].append(v); g[v].append(u)
    dp=[[0,0] for _ in range(n)]
    vis=[False]*n
    def dfs(u):
        vis[u]=True; dp[u][1]=1
        for v in g[u]:
            if not vis[v]:
                dfs(v); dp[u][0]+=max(dp[v]); dp[u][1]+=dp[v][0]
    dfs(0)
    return max(dp[0])

if __name__ == "__main__":
    print(tree_mis(6,[(0,1),(0,2),(1,3),(1,4),(2,5)]))
