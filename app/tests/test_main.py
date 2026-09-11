from app.main import calculate_total

def test_calculate_total():
    assert calculate_total(10,3) == 30

def test_zero_quantity():
    assert calculate_total(10,0) == 0

