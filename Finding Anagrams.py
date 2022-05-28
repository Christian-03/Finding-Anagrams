# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("race_car") --> True
print('This program checks to see if a word is an anagram.')

def find_anagrams():
    word = input('Enter first word: ')
    anagram = input('Enter second word: ')
    words = list()
    for char in word:
        words.append(char)
    anagrams = list()
    for char in anagram:
        anagrams.append(char)
    if sorted(words) == sorted(anagrams):
        return True
    else:
        return False

print(find_anagrams())