planet = "Earth"
# Yes, we can even loop over them
exclamation = [char+'! ' for char in planet]
# Searching for the first index of a substring
print(planet.index('t'))
print(planet.startswith('Ear'))
print(planet.endswith('th'))

sentence = "The quick brown fox jumps over the lazy dog"
sentence_words = sentence.split(' ')
print(sentence_words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
newdate = '/'.join([month, day, year])
# print(year, month, day)
print(newdate)

clapps = ' 👏 '.join([word.upper() for word in sentence_words])
print(clapps)

newformat = "The {} weighs {} pounds".format("dog", 10)
print(newformat)

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
pluto_sentence = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    "Pluto", pluto_mass, pluto_mass / earth_mass, population)
print(pluto_sentence)

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


print(help(str))


def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) >= 5 if zip_code.isdigit() else False

