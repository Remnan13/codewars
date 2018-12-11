'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

from string import ascii_lowercase
'''
Create paired keys(letters) and values(numbers)
Be sure to start at 1 -- not 0!
'''
letters_list = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start = 1)}

def alphabet_position(text):
#Convert all to lower case
    text = text.lower()
    result = [letters_list[element] for element in text if element in letters_list]
    return ' '.join(result)