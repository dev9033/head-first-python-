def search_for_vowels(word):
    """Display boolean based vowel found in an word"""  # doc string
    vowels = set('aeiou')

    found = vowels.intersection(set(word))
    return bool(found)


print(search_for_vowels(input()))
