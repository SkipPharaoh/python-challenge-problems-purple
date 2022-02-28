# Warmup - Even Range

```python
"""
*******************************************************************************
Write a function even_range(start, end) that returns an list containing all even
numbers between 'start' and 'end' in sequential order.
Examples:
even_range(13, 20) => [ 14, 16, 18, 20 ]
even_range(4, 11) => [ 4, 6, 8, 10 ]
even_range(8, 5) => []
*******************************************************************************/
"""


```

# Challenge Problem 0 - Phrase Finder

```python
"""
*******************************************************************************
Write a function phrase_finder(words, phrase), that takes in an list of words and a
string representing a phrase. The function should return True if the phrase can be
formed by a pair of words from the list. The function should return false if the
phrase cannot be formed by any pair of words.

Examples:

phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep') => True
phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye') => False
*******************************************************************************/
"""

```

 
# Challenge Problem 1 - hammingDistance

```py
"""
-----------------------------------------------------------------
Prompt:

In information theory, the hamming distance refers to the count of the differences between two strings of equal length.  It is used in computer science for such things as implementing "fuzzy search"  capability.

- Write a function named hammingDistance that accepts two arguments which are both strings of equal length.
- The function should return the count of the symbols (characters, numbers, etc.) at the same position within each string that are different.
- If the strings are not of the same length, the function should return NaN.

Examples:

hamming_distance('abc', 'abc'); //=> 0
hamming_distance('a1c', 'a2c'); //=> 1
hamming_distance('!!!!', '****'); //=> 4
hamming_distance('abc', 'ab'); //=> NaN

-----------------------------------------------------------------*/

"""
```

# Challenge Problem 2 - isPrime

```py


""" 
-----------------------------------------------------------------

Prompt:
- Write a function named isPrime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
- A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.

Examples:

isPrime(2) //=> true
isPrime(3) //=> true 
isPrime(4) //=> false
isPrime(29) //=> true
isPrime(200) //=> false

-----------------------------------------------------------------*/
"""
```

# Challenge Problem 3 - find_the_parity_outlier

```py
"""
-----------------------------------------------------------------

Prompt:
You are given an list (which will have a length of at least 3, but could be very large) containing integers. The list is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the list as an argument and returns this "outlier" N.

Examples
find_the_parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
Should return: 11 (the only odd number)

find_the_parity_outlier([160, 3, 1719, 19, 11, 13, -21])
Should return: 160 (the only even number)

-----------------------------------------------------------------*/

"""

```
