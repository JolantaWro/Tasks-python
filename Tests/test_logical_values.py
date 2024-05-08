import pytest
from Beginning.Operator.check_logical_values import check_logical_values

def test_equal():
    assert check_logical_values(2, "==", 2) == True

def test_not_equal():
    assert check_logical_values(2, "!=", 2) == False

def test_not_equal_false():
    assert check_logical_values(2, "!=", 3) == True

def test_less_than():
    assert check_logical_values(2, "<", 3) == True
 



