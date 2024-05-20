import pytest
from Beginning.String_Actions.string_actions import string_to_lower, string_to_upper, replace_words, find_words

def test_string_to_lower_success():
    assert string_to_lower("HELLO") == "hello"

def test_string_to_lower_failure():
    with pytest.raises(TypeError):
        string_to_lower(1)
    
def test_string_to_upper_success(): 
    assert string_to_upper("hello") == "HELLO"

def test_string_to_upper_failure():
    with pytest.raises(TypeError):
        string_to_upper(1)

def test_replace_word():
    text = "Hello world, this is a test."
    replacements = {"Hello": "Hi", "test": "sample"}
    result = replace_words(text, replacements)
    assert result == "Hi world, this is a sample."

def test_find_string_success():
    text = "Learning Python is fun and rewarding. Test-Driven Development helps write better code."
    word = "Python"
    result = find_words(text, word)
    assert result == True

def test_find_string_fail():
    text = "Learning language is fun and rewarding. Test-Driven Development helps write better code."
    word = "Python"
    result = find_words(text, word)
    assert result == True
