import pytest
from Beginning.Prework.prework_tasks import counter_add_value, counter_subtract_value

def test_counter_up():
    assert counter_add_value(5) == 6

def test_counter_down():
    assert counter_subtract_value(5) == 4
