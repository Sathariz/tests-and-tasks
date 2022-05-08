import pytest
from tasks.bracket_v2_01 import check_brackets

# @pytest.mark.parametrize(
#         ["bracket"],
#         [
#             ("{}[]"),
#             ("{[]({}[])]}"),
#             ("({}[()[{}]])"),
#             ("{()[]}[()]{[()]()}"),
#         ]
#     )

def test_check_brackets_01():
    actual = check_brackets("{}[]")

    expected = "Bracketastic!"

    assert expected == actual

def test_check_brackets_02():
    actual = check_brackets("{[]({}[])]}")

    expected = "Bracketastic!"

    assert expected == actual

def test_check_brackets_03():
    actual = check_brackets("({}[()[{}]])")

    expected = "Bracketastic!"

    assert expected == actual

def test_check_brackets_04():
    actual = check_brackets("{()[]}[()]{[()]()}")

    expected = "Bracketastic!"

    assert expected == actual