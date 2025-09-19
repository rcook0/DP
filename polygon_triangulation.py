"""
Minimum Weight Triangulation of Convex Polygon
"""
def polygon_triangulation(points):
    def dist2(a,b): return (a[0]-b[0])**2 + (a[1]-b[1])**2
    def tri_cost(i,j,k): 
        a,b,c = points[i], points[j], points[k]
        return dist2(a,b)+dist2(b,c)+dist2(c,a)
    n=len(points)
    dp=[[0]*n for _ in range(n)]
    for l in range(3, n+1):
        for i in range(n-l+1):
            j=i+l-1
            best=float('inf')
            for k in range(i+1, j):
                best=min(best, dp[i][k]+dp[k][j]+tri_cost(i,k,j))
            dp[i][j]=best
    return dp[0][n-1]

if __name__ == "__main__":
    pts=[(0,0),(1,0),(2,0),(2,1),(1,1),(0,1)]
    print(polygon_triangulation(pts))
