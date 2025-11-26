import app


def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 2) == 3

def test_multiply():
    assert app.multiply(4, 3) == 12

def test_divide():
    assert app.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        app.divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Division by zero"
