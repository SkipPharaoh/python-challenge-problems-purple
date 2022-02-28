# Warmup - Intersect

```python

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

def intersect(list1, list2) {
    # your code here...
```

# Challenge Problem 0 - Min Max Product

```python

"""
*******************************************************************************
Write a function `min_max_product(list)` that return the product between the
largest value and the smallest value in the list.

Assume `list` is an list of integers.
Assume an list of at least two integers.

Examples:

minMaxProduct([6, 3, 7, 2]) => 14
minMaxProduct([0, 1, -5, 3, 6]) => -30
******************************************************************************
"""

```



# Challenge 1 - find_highest_priced

```py

"""
-----------------------------------------------------------------

Prompt:

- Write a function named find_highest_priced that accepts a single list of dictionaries.
- The dictionaries contained in the list are guaranteed to have a price property holding a numeric value.
- The function should return the object in the list that has the largest value held in the price property.
- If there's a tie between two or more dictionaries, return the first of those dictionaries in the list.
- Return the original object, not a copy.

Examples:

find_highest_priced([
  { sku: 'a1', price: 25 },
  { sku: 'b2', price: 5 },
  { sku: 'c3', price: 50 },
  { sku: 'd4', price: 10 }
]);
//=> { sku: 'c3', price: 50 } 

find_highest_priced([
  { sku: 'a1', price: 25 },
  { sku: 'b2', price: 50 },
  { sku: 'c3', price: 50 },
  { sku: 'd4', price: 10 }
]);
//=> { sku: 'b2', price: 50 }

-----------------------------------------------------------------
"""
```

<br/><br/>

# Challenge 2 - balancedBrackets

```py

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
```

<br/><br/>

# Challenge 3 - count_the_bits

```py

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

```
<br/><br/>


