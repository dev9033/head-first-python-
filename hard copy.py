# copy method

li = [1, 2]
print("this is li {}".format(li))
li2 = li
print("this is li2 {}".format(li2))
li2.append(3)
print("this is li2 {}".format(li2))
print("no changes are made in li yet")
print("this is li {}".format(li))

print("copy method")

li3 = li2.copy()    # copy method
print("this is li3 {}".format(li3))
li3.append(4)
print("this is li3 {}".format(li3))
print("this is li2 {}".format(li2))
