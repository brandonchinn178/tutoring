"""
This skeleton code provides the overall framework for a Hangman game. Comments are provided
below to guide your implementation of the hangman function. In order to run this, you must
do the following things:

Install pip from https://pip.pypa.io/en/latest/installing.html (to check if you have pip,
    run `pip --version` on the command line or Terminal)
Run `sudo pip install RandomWords`. This will install a Python package on your system. To
    uninstall the package, run `pip uninstall RandomWords`.
To check your work and run the program, run `python hangman.py` in the same directory as
    this file (rename this file to be hangman.py)
"""

def draw_hangman(count=0):
    """
    Draws the following hangman, according to the count, with head being drawn first,
    then body, arms, legs.
     0
    /|\
    / \
    """
    figure = ' %(head)s \n%(leftarm)s%(body)s%(rightarm)s\n%(leftleg)s %(rightleg)s'
    head = '0' if count > 0 else ' '
    body = '|' if count > 1 else ' '
    leftarm = '/' if count > 2 else ' '
    rightarm = '\\' if count > 3 else ' '
    leftleg = '/' if count > 4 else ' '
    rightleg = '\\' if count > 5 else ' '
    print figure % {
        'head': head,
        'body': body,
        'leftarm': leftarm,
        'rightarm': rightarm,
        'leftleg': leftleg,
        'rightleg': rightleg
    }

def hangman(target):
    """
    Plays hangman with the given word as the solution
    """
    # the incorrect guessed letters
    incorrect = []
    # the correctly guessed letters
    correct = []
    while True:
        guess = raw_input("\nGuess a letter: ")
        if len(guess) > 1:
            print 'Please provide only one letter'
            continue

        # if the guessed letter is in the target word, add it to the correct-letters list
        # If the guessed letter is already in the correct-letters list, maybe print a message
        # instead of adding it again.

        # If the guessed letter is not in the target word, add it to the incorrect-letters
        # list. If there are at least 6 letters in the incorrect-letters list, print a
        # losing message to the player and exit the function

        # Draw the hangman here. See the draw_hangman function above and see what you
        # need to pass in to the function to print out the correct hangman

        # Build a new string by iterating through all of the letters in the target
        # word and replacing the letter with '_' if the letter is not in the correct-letters
        # list. Then print out this string so the player knows how far they are.
        # Advanced: see the map() function in Python

        # Find some way to check how you might now the game is over, and break from the loop
        # if the game is over.

if __name__ == "__main__":
    from random_words import RandomWords
    word = ''
    # keep words at least 5 letters long
    while len(word) < 5:
        word = RandomWords().random_word()
    hangman(word)