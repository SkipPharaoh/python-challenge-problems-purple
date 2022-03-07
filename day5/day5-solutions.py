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

def add_checker(items, sum):
    for num in items:
        for el in items:
            if num + el == sum:
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

"""
-----------------------------------------------------------------


Prompt:

- Write a function called total_task_time that accepts two arguments.
- The first argument is an list of integers referred to as a "queue".  Each integer in the queue represents a "task", more specifically, the amount of time to complete that task.
- The second argument is an integer representing the number of CPU "threads" available to process all of the tasks in the queue.
- The total_task_time function should return an integer representing the total time it is going to take to complete all of the tasks in the queue.
- You may mutate the "queue" list (first argument) if you wish.

Hint:

- Solve it with paper and pencil first.  Look for patterns and generalize.  Pseudocode!

Examples:

total_task_time( [], 1 ) // => 0
total_task_time( [4, 2, 5], 1 ) // => 11
total_task_time( [5, 8], 2 ) // => 8
total_task_time( [4, 2, 10], 2 ) // => 12
total_task_time( [2, 2, 3, 3, 4, 4], 2 ) //=> 9
total_task_time( [5, 2, 6, 8, 7, 2], 3 ) // => 12

-----------------------------------------------------------------
"""

def total_task_time(queue, threads):
    total = 0
    for i in range(len(queue)):
        total += queue[i]
    return total

print(total_task_time([], 1))
print(total_task_time([4, 2, 5], 1))
print(total_task_time([5, 8], 2))
print(total_task_time([4, 2, 10], 2))
print(total_task_time([2, 2, 3, 3, 4, 4], 2))
print(total_task_time([5, 2, 6, 8, 7, 2], 3))
