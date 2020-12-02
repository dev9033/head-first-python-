def search_for_vowels(word):
    """Display boolean based vowel found in an word"""  # doc string
    vowels = set('aeiou')
    # return a set of letters (one line code)
    return vowels.intersection(set(word))


print(search_for_vowels(input()))
