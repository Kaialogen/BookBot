import pytest
from stats import word_count, character_count, sorted_list

# ---------------------------
# word_count tests
# ---------------------------

@pytest.mark.parametrize("text, expected", [
    ("Hello World", 2),
    ("", 0),
    ("One two   three", 3),
    (" Leading and trailing spaces ", 4),
])
def test_word_count(text, expected):
    assert word_count(text) == expected


# ---------------------------
# character_count tests
# ---------------------------

@pytest.mark.parametrize("text, expected", [
    ("eeee", {"e": 4}),
    ("AaA", {"a": 3}),              # lowercasing behaviour
    ("ab ba", {"a": 2, "b": 2}),    # multiple words
])
def test_character_count(text, expected):
    assert character_count(text) == expected


# ---------------------------
# sorted_list tests
# ---------------------------

def test_sorted_list_basic():
    input_dict = {"a": 3, "b": 1, "c": 2}
    result = sorted_list(input_dict)

    expected = [
        {"char": "a", "num": 3},
        {"char": "c", "num": 2},
        {"char": "b", "num": 1},
    ]

    assert result == expected


def test_sorted_list_handles_empty():
    assert sorted_list({}) == []
