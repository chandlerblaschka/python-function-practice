# Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    # i captures key
    for i in kwargs:
        print(f'{i}:{kwargs[i]}')


name_args(a="writing", b="python", c="functions")

# Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.


def all_true(bool):
    return all(bool)

# return all returns true if all elements of a given iterable (list, dictionary, tuple, set, etc. ) are true


print(all_true((True, True, 1 == 1)))
print(all_true((True, False)))

# Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.


def one_true(bool):
    return any(bool)

# return any returns true if any element within an iterable is true


print(one_true([True, True, True]))
print(one_true([False, False, False]))
print(one_true((True, False)))

# Uses recursion to find the factorial of an integer.


def find_fact(num):
    if num < 1:
        print("invalid input")
    elif num == 1:
        return 1
    else:
        return(num * find_fact(num-1))


print(find_fact(5))

# Recursively removes all adjacent duplicate letters from a string.


def recursive_deduplicate(str, i=0):
    # print(str)
    if len(str) <= 1 or i == len(str)-1:
        return str
    else:
        if str[i] == str[i+1]:
            return recursive_deduplicate(str[0:i]+str[i+1:], i)
            # if the current position matches the next position the string is modified to exclude the i+1 value
        else:
            return recursive_deduplicate(str, i+1)


print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))


# Uses recursion to reverse a string.

def recursive_reverse(str, i=0):
    # empty string case
    if len(str) == 0:
        return ""
    # base case
    elif i == len(str)-1:
        return str[0]
    else:
        # recursive case
        return str[-1-i] + recursive_reverse(str, i+1)


print(recursive_reverse("aaaa"))
print(recursive_reverse("aaba"))
print(recursive_reverse("apple"))
print(recursive_reverse(""))

