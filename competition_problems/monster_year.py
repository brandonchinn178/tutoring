"""
A Monster Year is a 4-digit year when the first 2 digits + last 2 digits = middle 2 digits.

1978 is a Monster Year because 19 + 78 = 97 == 97
1979 is not a Monster Year because 19 + 79 = 98 != 97

To test your code, run `python monster_year.py` from the command line. To use the functions
from the interpreter, run `python -i monster_year.py` and you can use the functions
interactively.
"""

def is_monster_year(year):
    """
    Checks if the given year is a Monster Year

    @param year (int) -- the year to check. Assume the year is 4 digits.

    @returns (bool) True if the year is a Monster Year and False if the year is not.
    """
    # YOUR CODE HERE

def get_monster_year_between(start, end):
    """
    Gets every Monster Year between the two years. The start and the end years may be
    included in the search for a monster year

    @param start (int) -- the year to start checking from
    @param end (int) -- the year to end checking from

    @return (List<int>) a list of every Monster Year between the two years, inclusive
    """
    # YOUR CODE HERE

if __name__ == '__main__':
    import unittest

    class TestMonsterYear(unittest.TestCase):
        def test_is_monster_year(self):
            self.assertTrue(is_monster_year(1978))
            self.assertFalse(is_monster_year(1979))
            self.assertTrue(is_monster_year(2307))
            self.assertFalse(is_monster_year(1054))
            self.assertTrue(is_monster_year(4945))
            self.assertFalse(is_monster_year(5935))

        def test_get_monster_year_between(self):
            self.assertEqual(get_monster_year_between(1000, 1300), [1208])
            self.assertEqual(get_monster_year_between(1000, 1400), [1208, 1318])
            self.assertEqual(get_monster_year_between(5000, 6000), [5604, 5714, 5824, 5934])
            self.assertEqual(get_monster_year_between(1000, 1100), [])
            self.assertEqual(get_monster_year_between(1208, 1209), [1208])
            self.assertEqual(get_monster_year_between(7900, 8901), [7912, 8901])

    unittest.main()
