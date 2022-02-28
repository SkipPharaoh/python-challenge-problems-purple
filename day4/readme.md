# Warmup: Fuzz Bizz

```py
"""
******************************************************************************
Write a function fuzz_bizz(max) that returns an list of numbers under
the max. Each number should be either divisible by 2 or 7, BUT NOT BOTH.

Examples:
fuzz_bizz(17) => [ 2, 4, 6, 7, 8, 10, 12, 16 ]
fuzz_bizz(30) => [ 2, 4, 6, 7, 8, 10, 12, 16, 18, 20, 21, 22, 24, 26 ]
******************************************************************************
"""

```

# Challenge Problem 0 : Multiples

```py

"""
*******************************************************************************
Write a function that multiples(max, num) that takes in two integers. The function
should return an list of positive integers less than `max` that are multiples of `num`.

Examples:

multiples(10, 2) => [ 2, 4, 6, 8 ]
multiples(15, 3) => [ 3, 6, 9, 12 ]
******************************************************************************
"""


```

# Deliverable - Challenge 1 - flatten

```py

"""
-----------------------------------------------------------------
Prompt:

- Write a function named flatten that accepts a single list that may contain nested lists and returns a new "flattened" list.
- A flattened list is an list that contains no nested lists.
- lists maybe nested at any level.
- If any of the lists have duplicate values those duplicate values should be present in the returned list.
- The values in the new list should maintain their ordering as shown in the examples below.

Hint:

- This assignment provides an excellent opportunity to use recursion (a function that calls itself).  It can also be solved by using an inner function.

Examples:

flatten( [1, [2, 3]] );
#=> [1, 2, 3]  (a new list) 

flatten( [1, [2, [3, [4]]], 1, 'a', ['b', 'c']] );
#=> [1, 2, 3, 4, 1, 'a', 'b', 'c']

-----------------------------------------------------------------
"""
```

# Deliverable - Challenge 2 - is_winning_ticket

```py
"""
-----------------------------------------------------------------

Difficulty:  Intermediate

Prompt:

- Write a function called is_winning_ticket that accepts a single list an as argument.
- The input list represents a 'lottery ticket' consisting of one or more nested 2-value lists.  The first value of a nested list will be a string, the second an integer.
- The is_winning_ticket function should return true if all of the nested lists have a character in the string whose numeric character code equals the integer (2nd value).
- If any of the nested lists have a string where all of the character's character code does not match the integer, then return false.

Hint: Research ASCII conversion in python

Examples:

is_winning_ticket( [ ['ABC', 65] ] ) # => true
is_winning_ticket( [ ['ABC', 999], ['XY', 89] ] ) # => false
is_winning_ticket( [ ['ABC', 66], ['dddd', 100], ['Hello', 108] ] ) # => true
is_winning_ticket( [ ['ABC', 66], ['dddd', 15], ['Hello', 108] ] ) # => false

-----------------------------------------------------------------
"""
```

<br/><br/>  

#  Challenge 3 - grid_trip

```py

"""
-----------------------------------------------------------------

Difficulty:  Intermediate

Prompt:

- This challenge uses an imaginary grid where the x coordinate increases when you move 'up' and decreases when you move 'down'.  Similarly, the y coordinate increases when you move 'right' and decreases when you move 'left'.
- Write a function called grid_trip that accepts two arguments.
- The first argument is an list containing two integers.  The first represents the starting x position on the grid.  The second integer in the list represents the starting y position.
- The second argument is a string representing "moves" using the characters 'U', 'D', 'R' & 'L' to represent moving Up, Down, Right & Left respectively.  Each direction character will be followed by digits representing how many units to move in that direction.  For example, a string of 'D15R2U4' represents moving up 15 units, to the right 2 units, and finally, down 4 units.  The direction characters will always be upper case.
- The grid_trip function should return a new list of two integers: the final x position and the final y position.  Do not modify the list argument).

Hint: Research Reg Ex in python to 

Examples:

grid_trip( [0, 0], 'U2R1' ) # => [2, 1]
grid_trip( [5, 10], 'D5L15U2' ) #-> [2, -5]
grid_trip( [-22, 100], 'L2L15D50U1D9') #=> [-80, 83]
-----------------------------------------------------------------
"""
```







