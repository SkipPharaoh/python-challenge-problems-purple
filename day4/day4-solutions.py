# Problems Completed [ ]

# Your test/solution code here 

def fuzz_bizz(max):
    newList = []
    for i in range(max):
        if i % 2 == 0 and i % 7 != 0:
            newList.append(i)
        elif i % 7 == 0 and i % 2 != 0:
            newList.append(i)
    return newList

print(fuzz_bizz(17))
print(fuzz_bizz(30))

# Problem 0

def multiples(max, num):
    newList = []
    for i in range(2, max):
        if i % num == 0:
            newList.append(i)
    return newList

print(multiples(10, 2))
print(multiples(15, 3))

# Problem 1

def flatten(args):
    new_list=[]
    def make_flat(stuff):
        for item in stuff:
            if type(item) == list:
                make_flat(item)
            else:
                new_list.append(item)
    make_flat(args)
    print(new_list)
    return new_list
    

print(flatten([1, [2, 3]]))
print(flatten([1, [2, [3, [4]]], 1, 'a', ['b', 'c']]))

# Problem 2

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

def is_winning_ticket(ticket):
    for i in ticket:
        if i[0].find(chr(i[1])) == -1:
            return False
    return True

print(is_winning_ticket([['ABC', 65]]))
print(is_winning_ticket([['ABC', 999], ['XY', 89]]))
print(is_winning_ticket([['ABC', 66], ['dddd', 100], ['Hello', 108]]))
print(is_winning_ticket([['ABC', 66], ['dddd', 15], ['Hello', 108]]))

# Problem 3


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
