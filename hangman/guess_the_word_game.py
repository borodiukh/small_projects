from random import choice


def get_word():  # get one random word from text file
    with open('words_for_hangman.txt') as file:
        words_list = file.readlines()
        word = choice(words_list).upper().strip()
    return word


def display_hangman(tries):
    stages = [
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',

        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',

        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',

        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',

        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',

        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',

        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def input_from_user(propos, word):  # check user input for a "syntax" mistakes
    while not propos.isalpha() or (len(propos) != len(word) and len(propos) > 1):
        if not propos.isalpha():
            print('Only letters')
        if len(propos) != len(word) and len(propos) > 1:
            print('You input too short or too long word')
        propos = input('Input letter or word: ')


def maybe_new_game():
    new_game = input('Do you want to play new game? Input "yes" or "no" ')
    while new_game != 'yes' and new_game != 'no':
        new_game = input('Input "yes" or "no" ')
    return new_game


def play(word):  # main function, logic of the game

    word_completion = list('_' * len(word))  # array (all letters are '_')
    guessed_letters = []  # letters which was inputed before
    guessed_words = []  # words which was inputed before
    tries = 6
    print('LETS PLAY THE HANGMAN GAME')

    while True:

        print(display_hangman(tries))  # show state of the game
        print(''.join(word_completion))

        propos = input('Input letter or word: ')
        input_from_user(propos, word)  # check user input(FOR SYNTAX MISTAKES)
        propos = propos.upper()

        # if user input character or word which WAS BEFORE
        while (propos in guessed_letters) or (propos in guessed_words):
            print('You input this letter or word before')
            propos = input('Input letter or word: ')
            input_from_user(propos, word)
            propos = propos.upper()

        # check if the propos != word
        if len(propos) == len(word) and propos != word:
            tries -= 1
            guessed_words.append(propos)
            continue

        # if you guess letter
        if propos in word:
            guessed_letters.append(propos)

            for i in range(len(word)):
                if propos == word[i]:
                    word_completion[i] = word[i]

            # if you guessed all letters
            if '_' not in word_completion:
                print('CONGRATULATIONS, YOU WIN')

                # do you want to play new game
                new_game = maybe_new_game()
                global flag

                if new_game == 'yes':
                    flag = True
                    break
                elif new_game == 'no':
                    print('Goodbye, see you')
                    flag = False
                    break

        else:  # if letter not in word
            tries -= 1
            guessed_letters.append(propos)


        # if you guess the word or tries ended
        if propos == word or tries == 0:
            if propos == word:
                print('CONGRATULATIONS, YOU WIN')
            if tries == 0:
                print('You lose')
                print(f'The word : {word}')

            # do you want to play new game
            new_game = maybe_new_game()

            if new_game == 'yes':
                flag = True
                break
            elif new_game == 'no':
                print()
                print('Goodbye, see you')
                flag = False
                break


flag = True
while flag:
    play(get_word())