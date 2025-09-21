def cyk_parse(nterminals, productions, start_symbol, s):
    n=len(s)
    table=[[set() for _ in range(n)] for _ in range(n)]
    for i,ch in enumerate(s):
        for A, rhs_list in productions.items():
            for rhs in rhs_list:
                if isinstance(rhs, str) and rhs==ch:
                    table[i][i].add(A)
    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j=i+L-1
            for k in range(i, j):
                left=table[i][k]; right=table[k+1][j]
                for A, rhs_list in productions.items():
                    for rhs in rhs_list:
                        if isinstance(rhs, tuple) and len(rhs)==2:
                            X,Y=rhs
                            if X in left and Y in right:
                                table[i][j].add(A)
    return start_symbol in table[0][n-1] if n>0 else False
