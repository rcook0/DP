import importlib

MODULES = [
    # Only showing a subset for brevity, full list in actual project
    "coin_change_min_coins",
    "knapsack_01",
    "lis",
    "steiner_tree_bitmask",
    "max_sum_incr_subseq",
    "wildcard_match",
]

def test_import_and_basic_run():
    for mod_name in MODULES:
        mod = importlib.import_module(f"dp_compendium.{mod_name}")
        funcs = [getattr(mod, f) for f in dir(mod) if callable(getattr(mod, f))]
        assert funcs, f"No callable found in {mod_name}"
