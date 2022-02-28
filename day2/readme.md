# Warmup - Reverse String

```python
"""
******************************************************************************
Write a function reverse_string(string) that takes in a hyphenated string and
returns a the hyphenated string reversed.

Examples:
reverseString("Go-to-the-store") => "store-the-to-Go"
reverseString("Jump-jump-for-joy") => "joy-for-jump-Jump,"
******************************************************************************
"""

```

# Challenge Problem 0 - Is Element

```python

"""
*******************************************************************************
Write a function is_element(list, ele) that takes an list and an element.
The function should return the position if the element is found inside of the list, it
should return False otherwise.


Examples:

isElement([1,2,3,4,5], 5) => 4
isElement(["a", "b", "c"], "a") => 0
isElement(["a", "b", "c"], "d") => False
******************************************************************************
"""
```

# Challenge Problem 1 - merge_dictionaries

```py

"""
-----------------------------------------------------------------

Prompt:

- Write a function named merge_dictionaries that accepts at least two dictionaries as arguments, merges the properties of the second through n dictionaries into the first object, then finally returns the first dictionary.
- If any dictionaries have the same property key, values from the object(s) later in the arguments list should overwrite earlier values.

Examples:

merge_dictionaries({}, {a: 1});  //=> {a: 1} (same object as first arg)
merge_dictionaries({a: 1, b: 2, c: 3}, {d: 4});  //=> {a: 1, b: 2, c: 3, d: 4}
merge_dictionaries({a: 1, b: 2, c: 3}, {d: 4}, {b: 22, d: 44});  //=> {a: 1, b: 22, c: 3, d: 44}
-----------------------------------------------------------------
"""
```

<br/><br/>

# Challenge Problem 2 - prime_factors

```py
"""
-----------------------------------------------------------------


Prompt:

- Write a function named primeFactors that accepts a whole number greater than one (1) as an argument and returns an list of that argument's prime factors.
- The prime factors of a whole number are the prime numbers that, when multiplied together, equals the whole number.
- If the argument provided is not greater than 1, or not a whole number, then primeFactors should return an empty list.

Examples:

prime_factors(2) //=> [2]
prime_factors(3) //=> [3]
prime_factors(4) //=> [2, 2]
prime_factors(18) //=> [2, 3, 3]
prime_factors(29) //=> [29]
prime_factors(105) //=> [3, 5, 7]
prime_factors(200) //=> [2, 2, 2, 5, 5]

-----------------------------------------------------------------
"""
```

<br/><br/>

# Challenge Problem 3 - getNumForIP

```py
"""
-----------------------------------------------------------------

Prompt:

- Write a function called get_num_for_IP that accepts a single string as argument.
- The input string is formatted as an IP address, such as '192.156.99.15'.  IP addresses are used in networking and are actually 32-bit integers.  However, those that work with networks find it more convenient to work with these numbers as four 8-bit integers, separated by a 'dot' character.
- The getNumForIP function should return the numeric value of the string IP address being passed in as an argument.

Hints:

- Each 8-bit number can hold a value between 0 and 256.
- An IP's right most 8-bit number represents how many of 256 raised to the power of 0 (equals 1) there are.  The next 8-bit number represents how many of 256 raised to the power of 1 (256) there are, etc.  For example, if you took the right-most two 8-bit numbers of the IP address 192.156.99.15, you would have 15 * (256 ** 0), which equals 15, and 99 * (256**1), which equals 25344.
- To compute the numeric value for an IP address, you first compute the value for each of the four 8-bit chunks (as described in the above hint), and add them together!

Examples:

get_num_for_IP( '0.0.0.1' ) // => 1
get_num_for_IP( '0.0.2.0' ) // => 512
get_num_for_IP( '192.156.99.15' ) // => 3231474447
get_num_for_IP( '10.0.0.1' ) // => 167772161

-----------------------------------------------------------------

"""

```

<br/><br/>
