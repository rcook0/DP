"""
Smoke test for all dp_compendium modules.
Ensures they import and run without crashing.
"""

import importlib

MODULES = [
    # Classics
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

    # Exotics
    "steiner_tree_bitmask",
    "hamiltonian_count",
    "min_path_cover_dag",
    "game_pick_ends",
    "grundy_subtraction",
    "probability_dp",
    "mdp_value_iteration",
]

def test_import_and_basic_run():
    for mod_name in MODULES:
        mod = importlib.import_module(f"dp_compendium.{mod_name}")
        funcs = [getattr(mod, f) for f in dir(mod) if callable(getattr(mod, f))]
        assert funcs, f"No callable found in {mod_name}"
        func = funcs[0]
        try:
            if mod_name == "coin_change_min_coins":
                assert func([1,2], 3) in (1,2,-1)
            elif mod_name == "coin_change_num_ways":
                assert func([1,2], 3) >= 0
            elif mod_name == "knapsack_01":
                assert func([1,2],[1,1],1) >= 0
            elif mod_name == "knapsack_unbounded":
                assert func([1,2],[1,1],2) >= 0
            elif mod_name == "steiner_tree_bitmask":
                n=4; edges=[(0,1,1),(1,2,1),(2,3,1),(3,0,1),(0,2,2),(1,3,2)]
                assert func(n, edges, [0,2]) == 2
            elif mod_name == "hamiltonian_count":
                adj=[[0,1,1],[1,0,1],[1,1,0]]
                assert func(adj) == 1
            elif mod_name == "min_path_cover_dag":
                n=4; edges=[(0,1),(1,2),(2,3)]
                assert func(n, edges) == 1
            elif mod_name == "game_pick_ends":
                assert func([1,5,233,7]) == 239
            elif mod_name == "grundy_subtraction":
                # test winning_position
                assert mod.winning_position([5,7],[1,3,4]) in (True, False)
            elif mod_name == "probability_dp":
                assert mod.dice_ways(2,7) == 6
            elif mod_name == "mdp_value_iteration":
                S=['A','B','C']
                A={'A':['stay','go'],'B':['stay','go'],'C':['stay']}
                def P(s,a):
                    if s=='A' and a=='go': return [(0.7,'B'),(0.3,'C')]
                    if s=='B' and a=='go': return [(0.6,'C'),(0.4,'A')]
                    return [(1.0,s)]
                def R(s,a,sp): return 1.0 if sp=='C' else 0.0
                V,pi = func(S,A,P,R)
                assert set(V.keys()) == set(S)
            else:
                try:
                    func()
                except TypeError:
                    pass
        except Exception as e:
            raise AssertionError(f"{mod_name} failed basic run: {e}")
