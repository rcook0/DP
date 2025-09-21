"""
Minimum Weight Triangulation of convex polygon
"""
def triangulation(points):
    def d2(a,b): return (a[0]-b[0])**2+(a[1]-b[1])**2
    def tri(i,j,k):
        a,b,c=points[i],points[j],points[k]
        return d2(a,b)+d2(b,c)+d2(c,a)
    n=len(points)
    dp=[[0]*n for _ in range(n)]
    for L in range(3,n+1):
        for i in range(n-L+1):
            j=i+L-1; best=float('inf')
            for k in range(i+1,j):
                best=min(best, dp[i][k]+dp[k][j]+tri(i,k,j))
            dp[i][j]=best
    return dp[0][n-1]

if __name__ == "__main__":
    print(triangulation([(0,0),(2,0),(3,1),(2,2),(0,2)]))
