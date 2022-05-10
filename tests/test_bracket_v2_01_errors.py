import pytest
from tasks.bracket_v2_01 import check_brackets

@pytest.mark.parametrize(
        ["bracket"],
        [
            ("{()}[)]",),
            ("<()>",),
            ("{9)[][()[()]]}",),
            ("[][({)]",),
            ("{[]({}[])]}",),
        ]
    )

def test_check_brackets(bracket):
    actual = check_brackets(bracket)

    expected = "Errors"

    assert expected == actual
