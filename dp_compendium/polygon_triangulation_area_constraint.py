def triangle_area(a,b,c):
    return abs((a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])))/2.0

def min_triangulation_perimeter_with_min_area(points, min_tri_area=0.0):
    # Convex polygon assumed.
    n=len(points)
    def d(P,Q): 
        return ((P[0]-Q[0])**2 + (P[1]-Q[1])**2) ** 0.5
    def perim(i,j,k):
        A,B,C=points[i],points[j],points[k]
        return d(A,B)+d(B,C)+d(C,A)
    INF=float('inf')
    dp=[[0.0]*n for _ in range(n)]
    for L in range(3,n+1):
        for i in range(n-L+1):
            j=i+L-1
            best=INF
            for k in range(i+1,j):
                area = triangle_area(points[i],points[k],points[j])
                if area+1e-12 < min_tri_area:
                    continue
                cand = dp[i][k] + dp[k][j] + perim(i,k,j)
                if cand<best: best=cand
            dp[i][j]=0.0 if (L==3 and best==INF) else best
    return dp[0][n-1]
