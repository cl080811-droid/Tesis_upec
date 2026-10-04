from src.counting.roi import point_in_polygon

def test_point_inside_polygon():
    polygon = [(0, 0), (100, 0), (100, 100), (0, 100)]
    assert point_in_polygon((50, 50), polygon)

def test_point_outside_polygon():
    polygon = [(0, 0), (100, 0), (100, 100), (0, 100)]
    assert not point_in_polygon((150, 50), polygon)

def test_empty_polygon_accepts_point():
    assert point_in_polygon((50, 50), [])
