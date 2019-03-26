names = ['a', 'b', 'c', 'd']

i = 1
for name in names:
    print(i, name)
    i += 1

#OR

for i, name in enumerate(names, start = 1):
    print(i, name)

for i, name in enumerate(names):
    print(i, name)