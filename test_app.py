from app import add

def test_addition_1():
    assert add(1,  2) ==  3

def test_addition_2():
    assert add(1,  2) !=  5

def test_addition_3():
    assert add(-1,  1) ==  0

def test_addition_4():
    assert add(0,  0) ==  0
