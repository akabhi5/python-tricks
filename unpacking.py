a, b = (1, 2)
print(a)
print(b)

'''in case of not using second value use _ to assign value otherwise compiler gives warning
that variable is not used'''
x, _ = (4, 5)
print(x)

a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)

a, b, *c, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(d)