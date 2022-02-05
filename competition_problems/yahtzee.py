"""
In this file, you will make a function that scores a set of cards, based on the following rules:

Five of a kind (5 of the same card)  = 4 times the sum of all five values
Large Straight (5 cards in sequence) = 40
Small Straight (4 cards in sequence) = 30
Four of a kind (4 of the same card)  = 3 times the sum of all five values
Full House (2 of one card and 3 of the other) = 4a + 3b, where a is the number that appears
    three times and b is the number that appears twice
Three of a kind (3 of the same card) = sum of all values
Two Pairs (2 sets of pairs of values) = max value (of all five values) + min value (of all
    five values)
One Pair (a pair of values) = max value of all five values
Otherwise, the score is the min value of all five values.

To test your code, run `python yahtzee.py` from the command line. To use the functions
from the interpreter, run `python -i yahtzee.py` and you can use the functions
interactively.
"""

def _get_score_five_of_a_kind(values):
    """
    If the values represent a five of a kind, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a five of a kind, or 0 if not a five of a kind

    Note: the underscore at the beginning of the function name means this is a helper
    function and isn't really a "major" function other people should worry about
    """
    # YOUR CODE HERE

def _get_score_large_straight(values):
    """
    If the values represent a large straight, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a large straight, or 0 if not a large straight
    """
    # YOUR CODE HERE

def _get_score_small_straight(values):
    """
    If the values represent a small straight, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a small straight, or 0 if not a small straight
    """
    # YOUR CODE HERE

def _get_score_four_of_a_kind(values):
    """
    If the values represent a four of a kind, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a four of a kind, or 0 if not a four of a kind
    """
    # YOUR CODE HERE

def _get_score_full_house(values):
    """
    If the values represent a full house, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a full house, or 0 if not a full house
    """
    # YOUR CODE HERE

def _get_score_three_of_a_kind(values):
    """
    If the values represent a three of a kind, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a three of a kind, or 0 if not a three of a kind
    """
    # YOUR CODE HERE

def _get_score_two_pairs(values):
    """
    If the values represent two pairs, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for two pairs, or 0 if not two pairs
    """
    # YOUR CODE HERE

def _get_score_pair(values):
    """
    If the values represent a pair, return the correct score, otherwise return 0.

    @param values (List<int>) -- a list of 5 values to check

    @returns (int) the score of the values for a pair, or 0 if not a pair
    """
    # YOUR CODE HERE

class Yahtzee(object):
    """
    This class will represent a 5x5 array of values. An example run through:

    values = [ [1, 2, 3, 4, 5],
               [2, 2, 2, 2, 2],
               [3, 3, 1, 2, 3],
               [3, 4, 4, 5, 5],
               [4, 4, 4, 4, 3] ]
    game = Yahtzee(values)

    game.get_row_score(0)     # return 40
    game.get_row_score(1)     # return 4 *10
    game.get_row_score(2)     # return 3+3+1+2+3
    game.get_row_score(3)     # return 3+5
    game.get_row_score(4)     # return 3*(4+4+4+4+3)
    game.get_col_score(0)     # return 30
    game.get_col_score(1)     # return 2+4
    game.get_col_score(2)     # return 30
    game.get_col_score(3)     # return 2+5
    game.get_col_score(4)     # return 2+5

    game.get_score()         # return 40+40+12+8+3*19+30+6+30+7+7
    """
    def __init__(self, values):
        """
        Initializes a new Yahtzee game with the given values

        @param values (List<List<int>>) -- a list of 5 lists, each list containing
            5 elements (see example). Each element is a number 1-9
        """
        # YOUR CODE HERE

    def get_row_score(self, row):
        """
        Gets the score of the given row. A row's value is the highest possible score
        it can get for any hand it has.

        @param row (int) -- the index of the row being scored.

        @returns (int) the score for this row
        """
        # YOUR CODE HERE

    def get_col_score(self, col):
        """
        Gets the score of the given column. A column's value is the highest possible score
        it can get for any hand it has.

        @param col (int) -- the index of the column being scored.

        @returns (int) the score for this column
        """
        # YOUR CODE HERE

    def get_score(self):
        """
        Returns the sum of all the scores of its rows and columns.

        @returns (int) the score of the game
        """
        # YOUR CODE HERE

if __name__ == '__main__':
    import unittest

    class TestYahtzee(unittest.TestCase):
        def test_helpers(self):
            self.assertEqual(_get_score_five_of_a_kind([1,1,1,1,1]), 20)
            self.assertEqual(_get_score_large_straight([1,2,3,4,5]), 40)
            self.assertEqual(_get_score_small_straight([1,2,3,4,6]), 30)
            self.assertEqual(_get_score_four_of_a_kind([4,3,4,4,4]), 69)
            self.assertEqual(_get_score_full_house([1,3,1,3,1]), 13)
            self.assertEqual(_get_score_three_of_a_kind([2,2,2,5,6]), 17)
            self.assertEqual(_get_score_two_pairs([2,2,3,3,5]), 7)
            self.assertEqual(_get_score_pair([5,5,1,7,6]), 7)
            
            self.assertEqual(_get_score_five_of_a_kind([1,2,3,4,5]), 0)

        def test_yahtzee(self):
            values = [ [1, 2, 3, 4, 5],
                       [2, 2, 2, 2, 2],
                       [3, 3, 1, 2, 3],
                       [3, 4, 4, 5, 6],
                       [4, 4, 4, 4, 1] ]
            game = Yahtzee(values)

            self.assertEqual(game.get_row_score(0), 40)
            self.assertEqual(game.get_row_score(1), 40)
            self.assertEqual(game.get_row_score(2), 12)
            self.assertEqual(game.get_row_score(3), 30)
            self.assertEqual(game.get_row_score(4), 51)
            self.assertEqual(game.get_col_score(0), 30)
            self.assertEqual(game.get_col_score(1), 6)
            self.assertEqual(game.get_col_score(2), 30)
            self.assertEqual(game.get_col_score(3), 7)
            self.assertEqual(game.get_col_score(4), 1)

            self.assertEqual(game.get_score(), 247)

    unittest.main()
