import unittest
from text_to_Morse_code_converter import text_to_morse_code


class TestTextToMorseCode(unittest.TestCase):

    def test_text_to_morse_code_with_known_input(self):
        self.assertEqual(text_to_morse_code('Hello world'),
                         '.... . .-.. .-.. ---  /  .-- --- .-. .-.. -.. ')

    def test_text_to_morse_code_with_untranslatable_input(self):
        self.assertEqual(text_to_morse_code('&@#'), ' #   #   #  ')

    def test_text_to_morse_code_with_part_untranslatable_input(self):
        self.assertEqual(text_to_morse_code('I love You:)'),
                         '..  /  .-.. --- ...- .  /  -.-- --- ..-  #   #  ')


if __name__ == '__main__':
    unittest.main()