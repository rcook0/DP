import dp_compendium.knapsack_01 as k01
import dp_compendium.knapsack_unbounded as ku

def test_knapsack_01():
    values, weights, W = [60,100,120], [10,20,30], 50
    assert k01.knapsack(values, weights, W) == 220

def test_knapsack_unbounded():
    values, weights, W = [10,30,20], [5,10,15], 60
    assert ku.knapsack_unbounded(values, weights, W) > 0
