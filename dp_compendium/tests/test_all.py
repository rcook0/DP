"""
Unified smoke test across all modules.
"""

import importlib

MODULES = [
    # Classics
    "coin_change_min_coins", "coin_change_num_ways",
    "knapsack_01", "knapsack_unbounded",
    "subset_sum", "partition_equal_subset",
    "lis", "lcs_traceback", "edit_distance",
    "rod_cutting", "house_robber",
    "longest_palindromic_subsequence", "palindrome_partitioning_min_cuts",
    "floyd_warshall_paths", "tsp_bitmask_path",
    "matrix_chain_reconstruct", "optimal_bst", "polygon_triangulation",
    "tree_max_independent_set", "egg_dropping", "painters_partition",
    "digit_dp_no_consecutive_equal", "sequence_alignment_traceback", "dtw",

    # Exotics
    "steiner_tree_bitmask", "hamiltonian_count", "min_path_cover_dag",
    "game_pick_ends", "grundy_subtraction", "probability_dp",
    "mdp_value_iteration",

    # Sequence / Array
    "max_sum_incr_subseq", "longest_bitonic_subseq",
    "max_submatrix_sum", "partition_array_max_sum",

    # Stringology
    "wildcard_match", "regex_match",
    "shortest_common_superseq", "distinct_subseq_count", "min_window_subseq",

    # New batch
    "digit_dp_sum_mod_k", "digit_dp_no_adjacent_zeros", "digit_dp_prime_sum",
    "partition_numbers", "polygon_triangulation_area_constraint",
    "dp_optimizations", "aliens_trick_partition",
    "viterbi_hmm", "cyk_parsing",
    "damerau_levenshtein", "affine_gap_alignment",
]

def test_import_and_has_functions():
    for mod_name in MODULES:
        mod = importlib.import_module(f"dp_compendium.{mod_name}")
        funcs = [f for f in dir(mod) if callable(getattr(mod, f))]
        assert funcs, f"No callable functions in {mod_name}"
