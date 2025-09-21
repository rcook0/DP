def needleman_wunsch_affine(a, b, match=1, mismatch=-1, gap_open=-2, gap_extend=-1):
    n,m=len(a),len(b)
    NEG=-10**9
    M=[[NEG]*(m+1) for _ in range(n+1)]
    Ix=[[NEG]*(m+1) for _ in range(n+1)]
    Iy=[[NEG]*(m+1) for _ in range(n+1)]
    M[0][0]=0
    for i in range(1,n+1):
        Ix[i][0]=gap_open + (i-1)*gap_extend
    for j in range(1,m+1):
        Iy[0][j]=gap_open + (j-1)*gap_extend
    for i in range(1,n+1):
        for j in range(1,m+1):
            sc = match if a[i-1]==b[j-1] else mismatch
            M[i][j]=max(M[i-1][j-1], Ix[i-1][j-1], Iy[i-1][j-1]) + sc
            Ix[i][j]=max(M[i-1][j]+gap_open, Ix[i-1][j]+gap_extend)
            Iy[i][j]=max(M[i][j-1]+gap_open, Iy[i][j-1]+gap_extend)
    return max(M[n][m], Ix[n][m], Iy[n][m])
