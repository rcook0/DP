# Dynamic Programming Compendium (Python)

A curated, GitHub‑ready collection of classic **and** exotic dynamic programming problems.
Each module contains:
- Problem statement
- DP state & recurrence in docstring
- Clean Python implementation (usually bottom‑up; some top‑down with memoization)
- A tiny self‑test/demo in `__main__`

## Contents

### Classics
- `coin_change_min_coins.py`
- `coin_change_num_ways.py`
- `lis.py` (Longest Increasing Subsequence)
- `lcs.py` (Longest Common Subsequence)
- `edit_distance.py` (Levenshtein)
- `knapsack_01.py`
- `knapsack_unbounded.py`
- `subset_sum.py`
- `partition_equal_subset.py`
- `rod_cutting.py`
- `house_robber.py`
- `longest_palindromic_subsequence.py`
- `palindrome_partitioning_min_cuts.py`

### Graphs & Paths
- `floyd_warshall.py` (All‑pairs shortest path)
- `tsp_bitmask.py` (Traveling Salesman with bitmask DP)

### Intervals & Matrices
- `matrix_chain_bottom_up.py`
- `matrix_chain_top_down.py`
- `optimal_bst.py`
- `polygon_triangulation.py`

### Trees & Structures
- `tree_max_independent_set.py`
- `egg_dropping.py`
- `painters_partition.py`

### Strings, Bioinformatics, Time Series
- `digit_dp_no_consecutive_equal.py`
- `sequence_alignment_needleman_wunsch.py`
- `dtw.py` (Dynamic Time Warping)

## How to run

```bash
python module_name.py
# e.g. python coin_change_min_coins.py
```

Each script prints a small demo result for sanity checking.

---

MIT License. Enjoy!

## Enhancements Included

- **Matrix Chain Multiplication**: optimal parenthesization reconstruction (`matrix_chain_reconstruct.py`).
- **Floyd–Warshall**: path reconstruction with a `next` (successor) matrix (`floyd_warshall_paths.py`).
- **Needleman–Wunsch**: full global alignment traceback (`sequence_alignment_traceback.py`).
- **Unit Tests**: `tests/` folder with `pytest` tests for correctness.

### Run tests
```bash
pip install pytest
pytest -q
```

---

### Examples

#### Matrix Chain
```python
from matrix_chain_reconstruct import matrix_chain_parenthesize
p = [30,35,15,5,10,20,25]
cost, parens = matrix_chain_parenthesize(p)
print(cost)   # 15125
print(parens) # ((A1(A2A3))((A4A5)A6)) or equivalent optimal structure
```

#### Floyd–Warshall Paths
```python
from floyd_warshall_paths import floyd_warshall_with_path
INF = 10**9
dist = [
    [0,3,INF,7],
    [8,0,2,INF],
    [5,INF,0,1],
    [2,INF,INF,0],
]
D, nxt = floyd_warshall_with_path(dist)
def get_path(u,v):
    if nxt[u][v] is None: return []
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path
print(get_path(0,3))  # e.g., [0,1,2,3] depending on weights
```

#### Needleman–Wunsch Traceback
```python
from sequence_alignment_traceback import needleman_wunsch_align
score, a_aln, b_aln = needleman_wunsch_align("GATTACA","GCATGCU", match=1, mismatch=-1, gap=-2)
print(score)
print(a_aln)
print(b_aln)
```
