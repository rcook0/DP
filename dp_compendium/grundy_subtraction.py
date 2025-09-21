def grundy_numbers(limit, moves):
    g=[0]*(limit+1)
    for n in range(1, limit+1):
        reach=set()
        for m in moves:
            if n>=m: reach.add(g[n-m])
        mex=0
        while mex in reach: mex+=1
        g[n]=mex
    return g

def winning_position(heaps, moves):
    g = grundy_numbers(max(heaps) if heaps else 0, moves)
    x=0
    for h in heaps: x ^= g[h]
    return x!=0
