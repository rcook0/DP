import click

# -----------------
# Import modules
# -----------------
from dp_compendium import (
    # Classics
    coin_change_min_coins, coin_change_num_ways,
    knapsack_01, knapsack_unbounded,
    subset_sum, partition_equal_subset,
    lis, lcs_traceback, edit_distance,
    rod_cutting, house_robber,
    longest_palindromic_subsequence, palindrome_partitioning_min_cuts,
    floyd_warshall_paths, tsp_bitmask_path,
    matrix_chain_reconstruct, optimal_bst, polygon_triangulation,
    tree_max_independent_set, egg_dropping, painters_partition,
    digit_dp_no_consecutive_equal, sequence_alignment_traceback, dtw,

    # Exotics
    steiner_tree_bitmask as steiner,
    hamiltonian_count as hc,
    min_path_cover_dag as mpc,
    game_pick_ends as gpe,
    grundy_subtraction as gs,
    probability_dp as pd,
    mdp_value_iteration as mdp,

    # Sequence / Array
    max_sum_incr_subseq as msis,
    longest_bitonic_subseq as lbs,
    max_submatrix_sum as mss,
    partition_array_max_sum as pams,

    # Stringology
    wildcard_match as wm,
    regex_match as rm,
    shortest_common_superseq as scs,
    distinct_subseq_count as dsc,
    min_window_subseq as mws,

    # New Digit DP / Combinatorics / Optimizations / NLP/Bio
    digit_dp_sum_mod_k, digit_dp_no_adjacent_zeros, digit_dp_prime_sum,
    partition_numbers as pn,
    polygon_triangulation_area_constraint as tri_area,
    dp_optimizations as dpo,
    aliens_trick_partition as atp,
    viterbi_hmm as vit,
    cyk_parsing as cyk,
    damerau_levenshtein as dl,
    affine_gap_alignment as aga,
)

@click.group()
def cli():
    """Dynamic Programming Compendium CLI"""
    pass

# Example groups kept short — add your demos here
@cli.group()
def digitdp():
    """Digit DP problems"""
    pass

@digitdp.command()
def sum_mod_k():
    print("Count:", digit_dp_sum_mod_k.count_sum_divisible_by_k(1000, 3))

@digitdp.command()
def no_adj_zeros():
    print("Count:", digit_dp_no_adjacent_zeros.count_no_adjacent_zeros(1000))

@digitdp.command()
def prime_sum():
    print("Count:", digit_dp_prime_sum.count_prime_digit_sum(1000))

@cli.group()
def combinatorics():
    """Combinatorial DP"""
    pass

@combinatorics.command()
def partitions():
    print("Stirling(5,2) =", pn.stirling2(5,2))
    print("Bell(5) =", pn.bell(5))

@cli.group()
def geometry():
    """Geometry / optimization DPs"""
    pass

@geometry.command()
def triang_area():
    poly=[(0,0),(2,0),(3,1),(2,2),(0,2)]
    print("Min perimeter:", tri_area.min_triangulation_perimeter_with_min_area(poly))

@geometry.command()
def optimizations():
    print("Knuth slimes:", dpo.knuth_opt_slimes([3,2,4,1]))

@geometry.command()
def aliens():
    print("Alien’s trick:", atp.minimize_largest_sum([7,2,5,10,8], 2))

@cli.group()
def nlp_bio():
    """NLP / Bioinformatics DP"""
    pass

@nlp_bio.command()
def viterbi_demo():
    states=['H','C']
    start={'H':0.6,'C':0.4}
    trans={'H':{'H':0.7,'C':0.3},'C':{'H':0.4,'C':0.6}}
    emit={'H':{'A':0.2,'B':0.8},'C':{'A':0.5,'B':0.5}}
    print("Path:", vit.viterbi(states,start,trans,emit,['A','B','A','B']))

@nlp_bio.command()
def cyk_demo():
    prods={'S':[('S','S'),'A'], 'A':['a']}
    print("CYK parse:", cyk.cyk_parse({'a'}, prods, 'S', 'aa'))

@nlp_bio.command()
def damerau_demo():
    print("DL distance:", dl.damerau_levenshtein("CA","AC"))

@nlp_bio.command()
def affine_demo():
    print("Affine gap alignment score:", aga.needleman_wunsch_affine("GATTACA","GCATGCU"))
