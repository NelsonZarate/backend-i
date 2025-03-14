from pytest import raises 
from session_6.exercise import multiplies_two_numbers

def test_multiplies_two_numbers() -> int:
    assert multiplies_two_numbers(2, 2) == 4


def test_multiplies_float_numbers():
    with raises(AssertionError,match="Multiplies of numbers must be type INT"):
        assert multiplies_two_numbers("a", 2)
