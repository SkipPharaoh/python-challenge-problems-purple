# Warmup - list Range

```python

"""
*******************************************************************************

Write a function list_range(min, max, step) that takes in 3 numbers as parameters
The function should return an list containing all numbers between `min` and `max`
at `step` intervals.
Examples:
list_range(0, 12, 2) => [ 0, 2, 4, 6, 8, 10, 12 ]
list_range(2, 5, 1) => [ 2, 3, 4, 5 ]
list_Range(100, 20, 3) => []
*******************************************************************************
"""

```

# Challenge 0 - Value Replace

```python

"""
*******************************************************************************
Write a function value_replace(list, dict) that takes in an list and an dictionary.
The function should return a new list where each element of the original list
is replaced with it's corresponding value from the dictionary.

Examples:

value_replace(['a', 'b', 'c', 'd'], {a: 1, b: 2, d: 4})
=> [ 1, 2, 'c', 4 ]

value_replace(['johnny', 'paula', 'tommy'], {paula: 'operations', johnny: 'manufacturing'})
=> [ 'manufacturing', 'operations', 'tommy' ]
******************************************************************************
"""

```

# Challenge Problem 1 - add_checker

```py

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


```


<br/><br/>


# Challenge Problem 2 - to_camel_case)  
```py
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
```
<br/><br/>

# Challenge Problem 3 - total_task_time

```py
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
```











