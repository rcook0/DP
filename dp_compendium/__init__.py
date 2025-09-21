"""
dp_compendium
=============

A curated collection of dynamic programming problems — classic and exotic —
with implementations, notebooks, and a pretty CLI.

Submodules include:
- lcs_traceback            : Longest Common Subsequence with traceback
- floyd_warshall_paths     : Floyd–Warshall with path reconstruction
- matrix_chain_reconstruct : Matrix Chain Multiplication with parenthesization
- tsp_bitmask_path         : Traveling Salesman (bitmask DP) with path recovery
- sequence_alignment_traceback : Needleman–Wunsch alignment with traceback
... plus many more (knapsack, LIS, coin change, egg dropping, etc.)

You can also run the CLI directly:
    dp-cli lcs --a abcdef --b ace
"""

__version__ = "0.1.0"

# Convenience imports for top-level access
from .lcs_traceback import lcs_with_trace
from .floyd_warshall_paths import floyd_warshall_with_path, reconstruct_path
from .matrix_chain_reconstruct import matrix_chain_parenthesize
from .tsp_bitmask_path import tsp_with_path
from .sequence_alignment_traceback import needleman_wunsch_align

__all__ = [
    "lcs_with_trace",
    "floyd_warshall_with_path",
    "reconstruct_path",
    "matrix_chain_parenthesize",
    "tsp_with_path",
    "needleman_wunsch_align",
]
