if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")

# Here's a slightly more succinct solution using a conditional expression:

print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")


def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number < 0 else False


def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return True if bool(ketchup) and bool(mustard) and bool(onion) else False

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return False if bool(ketchup) or bool(mustard) or bool(onion) else True

# One solution looks like:

# return not ketchup and not mustard and not onion
# We can also "factor out" the nots to get:

# return not (ketchup or mustard or onion)

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return True if ketchup ^ mustard else False # xor operation

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    sum = int(ketchup) + int(mustard) + int(onion)
    return True if sum == 1 else False

# This condition would be pretty complicated to express using just and, or and not, but using boolean-to-integer conversion gives us this short solution:

# return (int(ketchup) + int(mustard) + int(onion)) == 1
# Fun fact: we don't technically need to call int on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...

# return (ketchup + mustard + onion) == 1