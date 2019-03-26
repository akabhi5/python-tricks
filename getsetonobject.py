class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val)

print(person.first)

first = getattr(person, first_key)

print(first)

nperson = Person()

person_info = {'first': 'abhi', 'last': 'kr'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))