import dp_compendium.polygon_triangulation_area_constraint as tri
def test_runs():
    poly=[(0,0),(2,0),(3,1),(2,2),(0,2)]
    assert tri.min_triangulation_perimeter_with_min_area(poly,0.0) > 0
