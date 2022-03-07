# Problems Completed [ ]

# Your test/solution code here 

def list_range(min, max, step):
    new_list = []
    for i in range(min, max+1, step):
        new_list.append(i)
    return new_list

print(list_range(0, 12, 2))
print(list_range(2, 5, 1))
print(list_range(100, 20, 3))

# Problem 0

def value_replace(items, list_dict):
    new_list = []
    for item in items:
        if item in list_dict:
            new_list.append(list_dict[item])
        else:
            new_list.append(item)
    return new_list

print(value_replace(['a', 'b', 'c', 'd'], {'a': 1, 'b': 2, 'd': 4}))
print(value_replace(['johnny', 'paula', 'tommy'], {'paula': 'operations', 'johnny': 'manufacturing'}))


# Problem 1

"""
-----------------------------------------------------------------

Prompt:

- Write a function called add_checker that accepts two arguments.
- The first argument is an list containing at least two integers.  The integers in the list are sorted in ascending order.
- The second argument is an integer.
- The add_checker function should return true if there are two integers in the list of integers (first argument) that when added together, equals the integer passed in as the second argument.
- If there are no two integers in the list that sum up to equal the second argument, add_checker should return false.
Hint:
- An efficient solution can leverage the the fact that the integers in the list are sorted.

Examples:
add_checker( [1, 2], 3 ) // => true
add_checker( [-3, 2], 9 ) // => false
add_checker( [10, 15, 16, 22], 32 ) // => true
add_checker( [10, 15, 16, 22], 19 ) // => false
-----------------------------------------------------------------
"""

def add_checker(items, sum):
    for i in range(len(items)-1):
        if items[i] + items[i+1] == sum:
            return True
    return False

print(add_checker([1, 2], 3))
print(add_checker([-3, 2], 9))
print(add_checker([10, 15, 16, 22], 32))
print(add_checker([10, 15, 16, 22], 19))


# Problem 2

"""
-----------------------------------------------------------------

Difficulty:  Intermediate

Prompt:

- Write a function called to_camel_case that accepts a single string as argument.
- The to_camel-case function should return the string as camel-cased, removing each _ or - characters and capitalizing the character following the _ or -.

Hints:

- This is a great challenge for using regular expressions combined with the String.replace method.

Examples:

to_CamelCase( 'sei-rocks' ) // => 'wdiRocks'
to_CamelCase( 'banana_Turkey_potato' ) // => 'bananaTurkeyPotato'
to_CamelCase( 'Mama-mia' ) // => 'MamaMia'
to_CamelCase( 'A_b_c' ) // => 'ABC'
-----------------------------------------------------------------
"""

def to_camel_case(string):
    regular = string[0].split('_')
    for i in range(1, len(string)):
        if string[i] == '_':
            regular.append(string[i+1].upper())
        elif string[i] == '-':
            regular.append(string[i+1].upper())
        else:
            regular.append(string[i])
    return ''.join(regular)

print(to_camel_case('sei-rocks'))
print(to_camel_case('banana_Turkey_potato'))
print(to_camel_case('Mama-mia'))
print(to_camel_case('A_b_c'))



# Problem 3


