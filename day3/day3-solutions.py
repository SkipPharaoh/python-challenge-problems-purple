# Problems Completed [ ]

# Your test/solution code here 

"""
******************************************************************************
Write a function intersect(list1, list2) that takes in two lists and returns a
new list containing the elements common to both list1 and list2.

Hint: use index()

Examples:

intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']) => [ 'b', 'd' ]
intersect(['a', 'b', 'c'], ['x', 'y', 'z']) => []
*******************************************************************************/
"""

def intersect(list1, list2):
    newList = []
    for i in range(len(list1)):
        if list1[i] in list2:
            newList.append(list1[i])
    return newList

print(intersect(['a', 'b', 'c', 'd'], ['b', 'd', 'e']))
print(intersect(['a', 'b', 'c'], ['x', 'y', 'z']))

# Problem 0

def min_max_product(list):
    return min(list) * max(list)

print(min_max_product([6, 3, 7, 2]))
print(min_max_product([0, 1, -5, 3, 6]))

# Problem 1

def find_highest_priced(list):
    return max(list, key=lambda x: x['price'])

print(find_highest_priced([
  { 'sku': 'a1', 'price': 25 },
  { 'sku': 'b2', 'price': 5 },
  { 'sku': 'c3', 'price': 50 },
  { 'sku': 'd4', 'price': 10 }
]))
print(find_highest_priced([
  { 'sku': 'a1', 'price': 25 },
  { 'sku': 'b2', 'price': 50 },
  { 'sku': 'c3', 'price': 50 },
  { 'sku': 'd4', 'price': 10 }
]))

# Problem 2

"""
-----------------------------------------------------------------

Prompt:

- Write a function called balanced_brackets that accepts a single string as argument.
- The input string is composed entirely of parentheses, brackets and/or curly braces, i.e.,  (), [] and/or {}. Referred to as "braces" from this point forward...
- The balancedBraces function should return true if the string's braces are "balanced" and false if they are not.
- The brackets are considered unbalanced if any closing bracket does not close the same type of opening bracket, ignoring already matched brackets between them.  Examples explain it best...

Examples:

balanced_brackets( '()' ) // => true
balanced_brackets( '(]' ) // => false
balanced_brackets( '[{}]' ) // => true
balanced_brackets( '[(])' ) // => false
balanced_brackets( '[({}[])]' ) // => true

-----------------------------------------------------------------
"""

def balanced_brackets(string):
    stack = []
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for idx in string:
        if idx in "{[(":
            stack.append(idx)
        elif stack and idx == bracket_pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


print(balanced_brackets('()'))
print(balanced_brackets('(]'))
print(balanced_brackets('[{}]'))
print(balanced_brackets('[(])'))
print(balanced_brackets('[({}[])]'))

# Problem 3

"""
-----------------------------------------------------------------

Difficulty:  Intermediate

Prompt:

- Write a function called count_the_bits that accepts a single numeric argument that will be an integer.
- The function should return the number of bits that are set to 1 in the number's binary representation.

Hints:

- We typically work with "decimal" numbers on a daily basis. Decimal is "base 10", where there are 10 digits available - 0 thru 9.  However, it's binary that computers understand - 1's and 0's.  The 1's and 0's are called bits.
- As an example, the decimal value of 13 is represented in binary as 1101.  There are 3 one bits and 1 zero bit in the decimal number of 13.
- Carefully read the documentation for the Number.prototype.toString method.

Examples:

count_the_bits( 0 ) // => 0
count_the_bits( 13 ) // => 3
count_the_bits( 256 ) // => 1
count_the_bits( 255 ) //=> 8
count_the_bits( 65535 )  //=> 16
-----------------------------------------------------------------
"""

def count_the_bits(num):
    arr = []
    done = False
    while not done:
        arr.append(num % 2)
        num = num // 2
        if num == 0:
            done = True
    return arr.count(1)

print(count_the_bits(0))
print(count_the_bits(13))
print(count_the_bits(256))
print(count_the_bits(255))
print(count_the_bits(65535))

