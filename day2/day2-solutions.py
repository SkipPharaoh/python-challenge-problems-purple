# Problems Completed [ ]

# Your test/solution code here 

def reverse_string(string):
    reverseStr = string.split("-")
    reverseJoin = "-".join(reverseStr[::-1])
    return reverseJoin

print(reverse_string("Go-to-the-store"))
print(reverse_string("Jump-jump-for-joy"))

# Problem 0

def is_element(list, ele):
    for i in range(len(list)):
        if list[i] == ele:
            return i
    return False

print(is_element([1,2,3,4,5], 5))
print(is_element(["a", "b", "c"], "a"))
print(is_element(["a", "b", "c"], "d"))

# Problem 1

def merge_dictionaries(*args):
    for i in range(len(args)):
        for key, value in args[i].items():
            args[0][key] = value
    return args[0]

print(merge_dictionaries({}, {'a': 1}))
print(merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}))
print(merge_dictionaries({'a': 1, 'b': 2, 'c': 3}, {'d': 4}, {'b': 22, 'd': 44}))

# Problem 2

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

def primeFactors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num /= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num /= i
    if num > 2:
        factors.append(int(num))
    return factors

print(primeFactors(2))
print(primeFactors(3))
print(primeFactors(4))
print(primeFactors(18))
print(primeFactors(29))
print(primeFactors(105))
print(primeFactors(200))

# Problem 3

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

def get_num_for_IP(ip):
    ip = ip.split(".")
    answer = 0
    for i in range(len(ip)):
        answer += int(ip[i]) * (256 ** (3 - i))
    return answer

print(get_num_for_IP( '0.0.0.1' ))
print(get_num_for_IP( '0.0.2.0' ))
print(get_num_for_IP( '192.156.99.15' ))
print(get_num_for_IP( '10.0.0.1' )  )
