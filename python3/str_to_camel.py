'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''

def to_camel_case(text):
    if len(text) < 1:
        return ''
    a = text.replace('-', ' ').replace('_', ' ')
    s = a.split()
    index = 1
    while index < len(s):
        s[index] = s[index].capitalize()
        index += 1
    result = ''.join(s)
    return result