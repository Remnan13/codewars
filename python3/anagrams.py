'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''

'''
Pseudocode: 
compare array element to target word, 
--need to account for duplicate chars
---sorted() compare?
return element to new_array if true
'''
# def anagrams(word, words):
#     sorted_word = sorted(word)
#     new_arr = []
#     for element in words:
#         sorted_element = sorted(element)
#         if sorted_element == sorted_word:
#             new_arr.append(element)
#             print("%s is an anagram of %s" % (element, word))
#         else:
#             print("%s is NOT an anagram of %s" % (element, word))
#     return new_arr

def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]