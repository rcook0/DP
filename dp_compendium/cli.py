import argparse, ast
from rich.console import Console
from rich.table import Table
from rich.text import Text

from .lcs_traceback import lcs_with_trace
from .floyd_warshall_paths import floyd_warshall_with_path, reconstruct_path
from .matrix_chain_reconstruct import matrix_chain_parenthesize
from .tsp_bitmask_path import tsp_with_path
from .sequence_alignment_traceback import needleman_wunsch_align

console = Console()

def cmd_lcs(args):
    n, s = lcs_with_trace(args.a, args.b)
    table = Table(title="Longest Common Subsequence")
    table.add_column("Length", justify="right")
    table.add_column("Subsequence", justify="left")
    table.add_row(str(n), s)
    console.print(table)

def cmd_floyd(args):
    mat = ast.literal_eval(args.matrix)
    D, nxt = floyd_warshall_with_path(mat)
    table = Table(title="All-Pairs Shortest Paths")
    for j in range(len(D)): table.add_column(str(j))
    for i,row in enumerate(D):
        table.add_row(*[str(x if x<1e8 else "∞") for x in row])
    console.print(table)
    if args.path:
        u,v = map(int, args.path.split(","))
        path = reconstruct_path(nxt, u, v)
        console.print(f"Shortest path {u} → {v}: [bold cyan]{' → '.join(map(str,path))}[/]")

def cmd_matrix_chain(args):
    p = ast.literal_eval(args.p)
    cost, parens = matrix_chain_parenthesize(p)
    console.print(f"[bold green]Optimal cost:[/] {cost}")
    console.print(f"[bold yellow]Parenthesization:[/] {parens}")

def cmd_tsp(args):
    mat = ast.literal_eval(args.matrix)
    cost, tour = tsp_with_path(mat)
    console.print(f"[bold green]TSP Cost:[/] {cost}")
    console.print("Tour: " + " → ".join(map(str, tour)))

def cmd_align(args):
    score, a_aln, b_aln = needleman_wunsch_align(args.a, args.b,
                                                 match=args.match,
                                                 mismatch=args.mismatch,
                                                 gap=args.gap)
    console.print(f"[bold green]Alignment score:[/] {score}")
    console.print(Text(a_aln, style="cyan"))
    console.print(Text(b_aln, style="magenta"))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("lcs"); sp.add_argument("--a", required=True); sp.add_argument("--b", required=True); sp.set_defaults(func=cmd_lcs)
    sp = sub.add_parser("floyd"); sp.add_argument("--matrix", required=True); sp.add_argument("--path"); sp.set_defaults(func=cmd_floyd)
    sp = sub.add_parser("matrix-chain"); sp.add_argument("--p", required=True); sp.set_defaults(func=cmd_matrix_chain)
    sp = sub.add_parser("tsp"); sp.add_argument("--matrix", required=True); sp.set_defaults(func=cmd_tsp)
    sp = sub.add_parser("align"); sp.add_argument("--a", required=True); sp.add_argument("--b", required=True)
    sp.add_argument("--match", type=int, default=1); sp.add_argument("--mismatch", type=int, default=-1); sp.add_argument("--gap", type=int, default=-2)
    sp.set_defaults(func=cmd_align)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
