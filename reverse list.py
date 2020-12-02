# list slices with [start,stop,step]

a = "don't panic!"
letters = list(a)

# all letters
print(letters)

# every 3rd letter upto index location 10 (10th not including)
print(letters[0:10:3])

# skip the first 3 letters and give everything
print(letters[3:])

# all letters upto 10th index but 10 is not including
print(letters[:10])

# every second letters
print(letters[::2])
