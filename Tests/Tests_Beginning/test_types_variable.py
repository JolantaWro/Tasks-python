import pytest
from Beginning.Types.variable_types import check_type
from Beginning.Function.take_and_check import take_return_type

def test_check_type():
    assert check_type(5) == "int"
    assert check_type("hello") == "str"
    assert check_type([1, 2, 3]) == "list"

def test_get_data_and_return_int():
    user_info = 5
    assert take_return_type(user_info) == "int"

def test_get_data_and_return_str():
    user_info = "Hi"
    assert take_return_type(user_info) == "str"
