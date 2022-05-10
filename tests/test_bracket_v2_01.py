import pytest
from tasks.bracket_v2_01 import check_brackets

@pytest.mark.parametrize(
        ["bracket"],
        [
            ("{}[]",),
            ("{[]({}[])}",),
            ("({}[()[{}]])",),
            ("{()[]}[()]{[()]()}",),
        ]
    )

def test_check_brackets(bracket):
    actual = check_brackets(bracket)

    expected = "Bracketastic!"

    assert expected == actual
