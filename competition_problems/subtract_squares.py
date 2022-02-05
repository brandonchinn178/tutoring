"""
Consider a sequence that is created by starting with a positive integer and continually
subtracting the largest square less than or equal to the number until 0 is reached. For
example with 55:

55 - 49 = 6
6 - 4 = 2
2 - 1 = 1
1 - 1 = 0

To test your code, run `python subtract_squares.py` from the command line. To use the functions
from the interpreter, run `python -i subtract_squares.py` and you can use the functions
interactively.
"""

def number_of_iterations(num):
    """
    Returns the number of iterations the above sequence should be run before reaching 0.
    For 55, there are 4 iterations.

    @param num (int) -- the number to start at. The number is a positive integer.

    @returns (int) the number of iterations before reaching 0
    """
    # YOUR CODE HERE

def min_value_with_n_iterations(n):
    """
    Finds the min value that iterates through the sequence the given number of times.

    @param n (int) -- the number of iterations the value must iterate through

    @returns (int) the smallest value that satisfies number_of_iterations(4)
    """
    # YOUR CODE HERE

if __name__ == '__main__':
    import unittest

    class TestSequence(unittest.TestCase):
        def test_number_of_iterations(self):
            self.assertEqual(number_of_iterations(55), 4)
            self.assertEqual(number_of_iterations(4), 1)
            self.assertEqual(number_of_iterations(0), 0)
            self.assertEqual(number_of_iterations(10), 2)

        def test_min_value_with_n_iterations(self):
            self.assertEqual(min_value_with_n_iterations(0), 0)
            self.assertEqual(min_value_with_n_iterations(1), 1)
            self.assertEqual(min_value_with_n_iterations(2), 2)
            self.assertEqual(min_value_with_n_iterations(3), 3)
            self.assertEqual(min_value_with_n_iterations(4), 7)

    unittest.main()
