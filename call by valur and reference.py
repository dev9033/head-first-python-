# call by value and call by reference

def double(arg):
    print('before: ', arg)
    arg = arg*2
    print('after: ', arg)


def change(arg):
    print('before: ', arg)
    arg.append('more data')
    print('after: ', arg)


double(10)
double("saying ")
numbers = [42, 256, 16]
double(numbers)
print(numbers)

numbers = [42, 256, 16]
change(arg=numbers)
print(numbers)
