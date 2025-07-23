from src.math_operators import add , sub

def test_add():
    assert add(2,3) == 5
    assert add(-5,3) == -2

def test_sub():
    assert sub(3,5) == -2
    assert sub(4,2) == 2


