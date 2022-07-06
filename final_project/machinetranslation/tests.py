import unittest

from translator import english_to_french, french_to_english

class test_translator(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

    def test2(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')

    def test3(self):
        self.assertEqual(english_to_french('How Are You'), 'Comment ça va')

    def test4(self):
        self.assertEqual(french_to_english('Comment ça va'), 'How Are You')

if __name__ == '__main__':
    unittest.main()

