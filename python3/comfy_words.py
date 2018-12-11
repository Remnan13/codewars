'''
A comfortable word is a word which you can type always alternating the hand you type with 
(assuming you type using a QWERTY keyboard).

Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
Right: y, u, i, o, p, h, j, k, l, n, m

That being said, create a function which receives a word and returns true/True if it's a comfortable word and false/False otherwise.

The word will always be a string consisting of only ascii letters from a to z.
'''

def comfortable_word(word):
  left_letters = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
  right_letters = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
  count = 0
  comfy = True
  for letter in range(len(word)):
      if count == len(word)-1:
          return comfy
      if word[count] in left_letters and word[count+1] in left_letters:
          return False
      if word[count] in right_letters and word[count+1] in right_letters:
          return False
      else:
          comfy = True
      count += 1
  return comfy