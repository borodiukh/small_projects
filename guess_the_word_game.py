from random import choice

words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
              "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница",
              "магазин", "председатель", "сотрудник", "республика", "личность"]


def get_word(words):  # get one random word from words_list
    return choice(words).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
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


def input_from_user(propos, word):
    while not propos.isalpha() or (len(propos) != len(word) and len(propos) > 1):
        if not propos.isalpha():
            print('Not a character')
        if len(propos) != len(word) and len(propos) > 1:
            print('Ви ввели занадто коротке слово or too long word')
        propos = input('Введіть букву або слово: ')


def maybe_new_game():
    new_game = input('Do you want to play new game? Input "yes" or "no" ')
    while new_game != 'yes' and new_game != 'no':
        new_game = input('Input "yes" or "no" ')

    return new_game


def play(word):  # main function, logic of the game

    word_completion = list('_' * len(word))  # array, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    print('Давайте играть в угадайку слов!')

    while True:

        print(display_hangman(tries))  # show stan of the game
        print(''.join(word_completion))
        # print(word)  # SHOULD REMOVE LATER!!!

        propos = input('Введіть букву або слово: ')
        input_from_user(propos, word)  # check user input(FOR MISTAKES)
        propos = propos.upper()

        # if user input character or word which WAS BEFORE
        while (propos in guessed_letters) or (propos in guessed_words):
            print('Ви вводили цю букву або слово раніше')
            propos = input('Введіть букву або слово: ')
            input_from_user(propos, word)
            propos = propos.upper()

        # check if the propos == word
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
                print('Поздравляем, вы угадали слово! Вы победили!')

                # do you want to play new game
                new_game = maybe_new_game()
                global flag

                if new_game == 'yes':
                    flag = True
                    break
                elif new_game == 'no':
                    print('Goodbye')
                    flag = False
                    break
                    
        else:  # if letter not in word
            tries -= 1
            guessed_letters.append(propos)


        # if you guess the word or tries ended
        if propos == word or tries == 0:
            if propos == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
            if tries == 0:
                print('You lose')
                print(f'The word : {word}')

            # do you want to play new game
            new_game = maybe_new_game()

            if new_game == 'yes':
                flag = True
                break
            elif new_game == 'no':
                print('Goodbye')
                flag = False
                break


flag = True
while flag:
    play(get_word(words_list))