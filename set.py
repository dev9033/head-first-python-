# vowel checker
vowels = set('aeiou')
word = input('give a word: ')

# checking if their's any element of `word` in `vowels`
found = vowels.intersection(set(word))

for i in found:
    print(i)
