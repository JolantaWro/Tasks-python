import pytest
from Beginning.Operations_Math.calculates import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, mean_numbers, median_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    with pytest.raises(TypeError):
        add_numbers("3", 9)

def test_subtract_numbers():
    assert subtract_numbers(2, 1) == 1
    with pytest.raises(TypeError):
        subtract_numbers("3", 9)

def test_multiply_numbers():
    assert multiply_numbers(2, 2) == 4
    with pytest.raises(TypeError):
        multiply_numbers("3", 9)

def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    with pytest.raises(TypeError):
        divide_numbers("3", 9)
    with pytest.raises(ValueError):
        divide_numbers(4, 0)

def test_mean_numbers():
    assert mean_numbers([4, 2, 3]) == 3
    with pytest.raises(ValueError):
        mean_numbers([])
    with pytest.raises(TypeError):
        mean_numbers([1, 'two', 3])

def test_median_odd_number_of_elements():
    assert median_numbers([1, 3, 5]) == 3
    assert median_numbers([3, 1, 5, 7, 9]) == 5

def test_median_even_number_of_elements():
    assert median_numbers([1, 3, 5, 7]) == 4
    assert median_numbers([1, 3, 5, 7, 2, 4]) == 3.5

def test_median_empty_list():
    with pytest.raises(ValueError):
        median_numbers([])

def test_median_non_numeric_elements():
    with pytest.raises(TypeError):
        median_numbers([1, 2, 'three', 4])
