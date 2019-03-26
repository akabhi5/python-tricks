names = ['Peter Parker', 'Clarke Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

#OR

'''here all the list are of same length. in case of varying length zip will stop after shortest list
or use zip from itertools library to reach longest list'''

'''zip is actually returning tuple of three of values'''
for name, hero, universes in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universes}')