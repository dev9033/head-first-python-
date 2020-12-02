# function annotations are optional, informational but they don't imply any other behaviour (such as type checking)

# :str represents that function will take a string and -> represents that it will return a set
def search4vowels(word: str) -> set:
    """Return any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


"""python interpreter isn't going to use annotations to check the type of function's arguments and its return type, then why we use it?
    The goal of annotations is not to make life easier for the interpreter; it's to make life easier for the user of your function. Annotations are a documentation standard, not a type enforcement mechanism.
It is used so that programmers know the expected input and return types, without reading the code inside it"""

print(search4vowels(input()))
