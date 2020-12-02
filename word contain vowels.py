# checking  if word contain vowels and printing it once

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('give a word to check for vowel: ')
found_vowels = []

for letter in word:
    if letter in vowels:
        if letter not in found_vowels:
            found_vowels.append(letter)
            print(letter)

if len(found_vowels) == 0:
    print('no vowel ')
