numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

# adding a new element
numbers['eleven'] = 11

# modifying an existing element
numbers['one'] = 'Pluto'

print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

print('Earth' in planet_to_initial)
print('Xenon' in planet_to_initial)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
sort = ' '.join(sorted(planet_to_initial.values())) # we could also use .keys()
print(sort)
