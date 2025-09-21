import argparse, ast, json
from lcs_traceback import lcs_with_trace
from floyd_warshall_paths import floyd_warshall_with_path, reconstruct_path
from matrix_chain_reconstruct import matrix_chain_parenthesize
from tsp_bitmask_path import tsp_with_path
from sequence_alignment_traceback import needleman_wunsch_align

def cmd_lcs(args):
    n, s = lcs_with_trace(args.a, args.b)
    print(json.dumps({"length": n, "subsequence": s}, ensure_ascii=False))

def cmd_floyd(args):
    mat = ast.literal_eval(args.matrix)
    D, nxt = floyd_warshall_with_path(mat)
    print(json.dumps({"dist": D}, ensure_ascii=False))
    if args.path:
        u,v = map(int, args.path.split(','))
        path = reconstruct_path(nxt, u, v)
        print(json.dumps({"path": path}, ensure_ascii=False))

def cmd_matrix_chain(args):
    p = ast.literal_eval(args.p)
    cost, parens = matrix_chain_parenthesize(p)
    print(json.dumps({"cost": cost, "parenthesization": parens}, ensure_ascii=False))

def cmd_tsp(args):
    mat = ast.literal_eval(args.matrix)
    cost, tour = tsp_with_path(mat)
    print(json.dumps({"cost": cost, "tour": tour}, ensure_ascii=False))

def cmd_align(args):
    score, a_aln, b_aln = needleman_wunsch_align(args.a, args.b, match=args.match, mismatch=args.mismatch, gap=args.gap)
    print(json.dumps({"score": score, "a": a_aln, "b": b_aln}, ensure_ascii=False))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("lcs"); sp.add_argument("--a", required=True); sp.add_argument("--b", required=True); sp.set_defaults(func=cmd_lcs)
    sp = sub.add_parser("floyd"); sp.add_argument("--matrix", required=True); sp.add_argument("--path", help="u,v"); sp.set_defaults(func=cmd_floyd)
    sp = sub.add_parser("matrix-chain"); sp.add_argument("--p", required=True); sp.set_defaults(func=cmd_matrix_chain)
    sp = sub.add_parser("tsp"); sp.add_argument("--matrix", required=True); sp.set_defaults(func=cmd_tsp)
    sp = sub.add_parser("align"); 
    sp.add_argument("--a", required=True); sp.add_argument("--b", required=True)
    sp.add_argument("--match", type=int, default=1); sp.add_argument("--mismatch", type=int, default=-1); sp.add_argument("--gap", type=int, default=-2)
    sp.set_defaults(func=cmd_align)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
