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
    incorrect = []
    correct = []
    while True:
        guess = raw_input("\nGuess a letter: ")
        if len(guess) > 1:
            print 'Please provide only one letter'
            continue
        if guess in target:
            if guess in correct:
                print "You've already guessed that correct letter"
            else:
                correct.append(guess)
        else:
            if guess in incorrect:
                print "You've already guessed that incorrect letter"
            else:
                incorrect.append(guess)
                if len(incorrect) == 6:
                    print "You lost :( the word was: %s" % target
                    return

        print 'Incorrect: %s' % ', '.join(incorrect)
        draw_hangman(len(incorrect))
        result = map(lambda letter: letter if letter in correct else '_', target)
        print ''.join(result)
        if '_' not in result:
            print 'You solved it!'
            break

if __name__ == "__main__":
    from random_words import RandomWords
    word = ''
    # keep words at least 5 letters long
    while len(word) < 5:
        word = RandomWords().random_word()
    hangman(word)