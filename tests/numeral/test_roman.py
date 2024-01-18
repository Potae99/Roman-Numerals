"""Test cases for Roman numerals."""

# Standard library


# 3rd Part library
import pytest

#Project library

from numeral.roman import to_roman


#----------------------------------------------

def test_calling_function():
    """Call a roman numeral function."""


#------------------------------------------------------
@pytest.mark.parametrize(
    "arabic_num, roman_num",
    [
        # Base case
        (1, "I"),
        (5, "V"),
        (10, "X")
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),

        # Additive case
        (2, "II"),
        (3, "III"),
        (6, "VI"),

        # Subtraction case
        (4,"IV"),
        (9,"IX"),
    ]
)
def test_to_roman(arabic_num, roman_num):
    """Convert Hindo-Arabic number to Roman number."""
    #Arrange


    #Act

    result = to_roman(arabic_num)


    #Assret
    assert result == roman_num
