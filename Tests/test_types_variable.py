import pytest
from Beginning.Types.variable_types import check_type

def test_check_type():
    assert check_type(5) == "int"
    assert check_type("hello") == "str"
    assert check_type([1, 2, 3]) == "list"