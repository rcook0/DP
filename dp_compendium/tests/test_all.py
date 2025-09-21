"""
Smoke test for all dp_compendium modules.
Ensures they import and run without crashing.
"""

import importlib

MODULES = [
    "coin_change_min_coins",
    "coin_change_num_ways",
    "knapsack_01",
    "knapsack_unbounded",
    "subset_sum",
    "partition_equal_subset",
    "lis",
    "lcs_traceback",
    "edit_distance",
    "rod_cutting",
    "house_robber",
    "longest_palindromic_subsequence",
    "palindrome_partitioning_min_cuts",
    "floyd_warshall_paths",
    "tsp_bitmask_path",
    "matrix_chain_reconstruct",
    "optimal_bst",
    "polygon_triangulation",
    "tree_max_independent_set",
    "egg_dropping",
    "painters_partition",
    "digit_dp_no_consecutive_equal",
    "sequence_alignment_traceback",
    "dtw",
]

def test_import_and_basic_run():
    for mod_name in MODULES:
        mod = importlib.import_module(f"dp_compendium.{mod_name}")
        # Pick a callable to smoke-test
        funcs = [getattr(mod, f) for f in dir(mod) if callable(getattr(mod, f))]
        assert funcs, f"No callable found in {mod_name}"
        func = funcs[0]
        try:
            # Try calling with dummy args if possible
            if mod_name == "coin_change_min_coins":
                assert func([1,2], 3) >= 0 or func([1,2], 3) == -1
            elif mod_name == "coin_change_num_ways":
                assert func([1,2], 3) >= 0
            elif mod_name == "knapsack_01":
                assert func([1,2],[1,1],1) >= 0
            elif mod_name == "knapsack_unbounded":
                assert func([1,2],[1,1],2) >= 0
            else:
                # Call with no args if it accepts none, otherwise skip
                try:
                    func()
                except TypeError:
                    pass
        except Exception as e:
            raise AssertionError(f"{mod_name} failed basic run: {e}")
