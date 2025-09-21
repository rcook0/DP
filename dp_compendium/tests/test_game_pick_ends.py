import dp_compendium.game_pick_ends as g

def test_game():
    assert g.optimal_first_player_score([1,5,233,7]) == 239
