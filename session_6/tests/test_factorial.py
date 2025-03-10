from pytest import raises
from session_6.challenge import factorial

def test_factorial_number_with_string():
    with raises(AssertionError,match=f"is not acceptable"):
        assert factorial("A")

def test_factorial_number_with_boolean():
    with raises(AssertionError,match=f" is not acceptable"):
        assert factorial(True)

def test_factorial_number():
    assert factorial(5) == 120

def  test_factorial_lesser_than_0():
    with raises(ValueError,match="number must be greater than 0"):
        assert factorial(-1)