import dp_compendium.rod_cutting as rc
import dp_compendium.house_robber as hr

def test_rod_cutting():
    assert rc.rod_cutting([1,5,8,9,10,17,17,20], 8) == 22

def test_house_robber():
    assert hr.house_robber([2,7,9,3,1]) == 12
