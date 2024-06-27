morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.-.'
}


def text_to_morse_code(string):
    """
        Converts a given text string to Morse code.

        Args:
            string (str): The input text to be converted to Morse code.

        Returns:
            str: The Morse code representation of the input text.
    """
    answer = ''
    for symbol in string.upper():
        if symbol in morse_code_dict:
            answer += morse_code_dict.get(symbol) + ' '
        elif symbol == ' ':
            # for separating words
            answer += ' /  '
        else:
            # for untranslatable character
            answer += ' #  '
    return answer


if __name__ == "__main__":

    print('\033[93mOutput description: program use spaces between letters, "/" between words and "#" for untranslatable character.\033[0m')
    user_input = input('Input message: ')
    morse_code_string = text_to_morse_code(user_input)
    print(f'Morse code:\n{morse_code_string}')
