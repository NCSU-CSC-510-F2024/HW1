def func(x):
    return x + 1

def test_passing():
    assert func(3) == 4

def test_failing():
    assert func(3) == 5