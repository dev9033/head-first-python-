# function in python
def search_for_vowels():
    """Display any vowels found in an asked-for word"""  # doc string
    vowels = set('aeiou')
    word = input('give a word to check search for vowel')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


search_for_vowels()
