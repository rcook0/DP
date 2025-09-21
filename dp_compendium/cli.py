import click

# -----------------
# Classics
# -----------------
from dp_compendium import (
    coin_change_min_coins,
    coin_change_num_ways,
    knapsack_01,
    knapsack_unbounded,
    subset_sum,
    partition_equal_subset,
    lis,
    lcs_traceback,
    edit_distance,
    rod_cutting,
    house_robber,
    longest_palindromic_subsequence,
    palindrome_partitioning_min_cuts,
    floyd_warshall_paths,
    tsp_bitmask_path,
    matrix_chain_reconstruct,
    optimal_bst,
    polygon_triangulation,
    tree_max_independent_set,
    egg_dropping,
    painters_partition,
    digit_dp_no_consecutive_equal,
    sequence_alignment_traceback,
    dtw,
)

# -----------------
# Exotics
# -----------------
from dp_compendium import (
    steiner_tree_bitmask as steiner,
    hamiltonian_count as hc,
    min_path_cover_dag as mpc,
    game_pick_ends as gpe,
    grundy_subtraction as gs,
    probability_dp as pd,
    mdp_value_iteration as mdp,
)

# -----------------
# Sequence / Array
# -----------------
from dp_compendium import (
    max_sum_incr_subseq as msis,
    longest_bitonic_subseq as lbs,
    max_submatrix_sum as mss,
    partition_array_max_sum as pams,
)

# -----------------
# Stringology
# -----------------
from dp_compendium import (
    wildcard_match as wm,
    regex_match as rm,
    shortest_common_superseq as scs,
    distinct_subseq_count as dsc,
    min_window_subseq as mws,
)


@click.group()
def cli():
    """Dynamic Programming Compendium CLI"""
    pass


# -----------------
# Classics group
# -----------------
@cli.group()
def classics():
    """Classic DP problems"""
    pass


@classics.command()
def coin_demo():
    print("Coin Change (min coins):", coin_change_min_coins.min_coins([1, 2, 5], 11))


@classics.command()
def knapsack_demo():
    print("Knapsack 0/1:", knapsack_01.knapsack([1, 2, 3], [6, 10, 12], 5))


@classics.command()
def lis_demo():
    print("LIS length:", lis.lis([10, 22, 9, 33, 21, 50, 41, 60]))


@classics.command()
def lcs_demo():
    print("LCS:", lcs_traceback.lcs("ABCBDAB", "BDCAB"))


@classics.command()
def edit_demo():
    print("Edit Distance:", edit_distance.edit_distance("kitten", "sitting"))


@classics.command()
def matrix_demo():
    arr = [40, 20, 30, 10, 30]
    print("Matrix Chain Multiplication:", matrix_chain_reconstruct.matrix_chain_order(arr))


# -----------------
# Exotics group
# -----------------
@cli.group()
def exotics():
    """Exotic / advanced DP problems"""
    pass


@exotics.command()
def steiner_demo():
    n = 4
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 2), (1, 3, 2)]
    print("Steiner cost:", steiner.steiner_tree_cost(n, edges, [0, 2]))


@exotics.command()
def hamiltonian_demo():
    adj = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    print("Hamiltonian cycles:", hc.count_hamiltonian_cycles(adj))


@exotics.command()
def pathcover_demo():
    n = 4
    edges = [(0, 1), (1, 2), (2, 3)]
    print("Min path cover:", mpc.min_path_cover_by_matching(n, edges))


@exotics.command()
def game_demo():
    arr = [1, 5, 233, 7]
    print("Optimal first-player score:", gpe.optimal_first_player_score(arr))


@exotics.command()
def grundy_demo():
    moves = [1, 3, 4]
    heaps = [5, 7]
    print("Position winning?", gs.winning_position(heaps, moves))


@exotics.command()
def prob_demo():
    print("P(H=3 before T=3):", pd.prob_heads_before_tails(3, 3))
    print("Ways (2 dice->7):", pd.dice_ways(2, 7))


@exotics.command()
def mdp_demo():
    S = ["A", "B", "C"]
    A = {"A": ["stay", "go"], "B": ["stay", "go"], "C": ["stay"]}

    def P(s, a):
        if s == "A" and a == "go":
            return [(0.7, "B"), (0.3, "C")]
        if s == "B" and a == "go":
            return [(0.6, "C"), (0.4, "A")]
        return [(1.0, s)]

    def R(s, a, sp):
        return 1.0 if sp == "C" else 0.0

    V, pi = mdp.value_iteration(S, A, P, R, 0.9)
    print("Values:", V)
    print("Policy:", pi)


# -----------------
# Sequence / Array group
# -----------------
@cli.group()
def sequence():
    """Sequence / Array DP problems"""
    pass


@sequence.command()
def msis_demo():
    arr = [1, 101, 2, 3, 100, 4, 5]
    print("MSIS:", msis.max_sum_incr_subseq(arr))


@sequence.command()
def bitonic_demo():
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    print("Longest Bitonic Subsequence:", lbs.longest_bitonic_subseq(arr))


@sequence.command()
def submatrix_demo():
    mat = [[1, -2, -1, 4], [-8, 3, 4, 2], [3, 8, 10, -8], [-4, -1, 1, 7]]
    print("Max Submatrix Sum:", mss.max_submatrix_sum(mat))


@sequence.command()
def partition_demo():
    arr = [1, 15, 7, 9, 2, 5, 10]
    K = 3
    print("Partition Array Max Sum:", pams.partition_array_max_sum(arr, K))


# -----------------
# Stringology group
# -----------------
@cli.group()
def string():
    """Stringology DP problems"""
    pass


@string.command()
def wildcard_demo():
    print("Wildcard Match:", wm.is_match("adceb", "*a*b"))


@string.command()
def regex_demo():
    print("Regex Match:", rm.is_regex_match("aab", "c*a*b"))


@string.command()
def scs_demo():
    print("Shortest Common Supersequence length:", scs.scs("abac", "cab"))


@string.command()
def distinct_demo():
    print("Distinct subsequences count:", dsc.num_distinct("rabbbit", "rabbit"))


@string.command()
def minwin_demo():
    print("Minimum Window Subsequence:", mws.min_window_subseq("abcdebdde", "bde"))
