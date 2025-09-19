"""
Needleman–Wunsch global alignment with traceback.

Returns:
  (score, aligned_a, aligned_b)
"""
def needleman_wunsch_align(a, b, match=1, mismatch=-1, gap=-2):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    # traceback pointers: 0 diag, 1 up, 2 left
    tb = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = i*gap
        tb[i][0] = 1
    for j in range(1,m+1):
        dp[0][j] = j*gap
        tb[0][j] = 2
    for i in range(1,n+1):
        for j in range(1,m+1):
            sc = match if a[i-1]==b[j-1] else mismatch
            diag = dp[i-1][j-1] + sc
            up = dp[i-1][j] + gap
            left = dp[i][j-1] + gap
            best = max(diag, up, left)
            dp[i][j] = best
            tb[i][j] = 0 if best==diag else (1 if best==up else 2)
    # traceback
    i, j = n, m
    a_aln, b_aln = [], []
    while i>0 or j>0:
        if i>0 and j>0 and tb[i][j]==0:
            a_aln.append(a[i-1]); b_aln.append(b[j-1])
            i-=1; j-=1
        elif i>0 and (j==0 or tb[i][j]==1):
            a_aln.append(a[i-1]); b_aln.append('-')
            i-=1
        else:
            a_aln.append('-'); b_aln.append(b[j-1])
            j-=1
    return dp[n][m], ''.join(reversed(a_aln)), ''.join(reversed(b_aln))

if __name__ == "__main__":
    score, a_aln, b_aln = needleman_wunsch_align("GATTACA","GCATGCU", match=1, mismatch=-1, gap=-2)
    print(score); print(a_aln); print(b_aln)
