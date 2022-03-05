# Warmup - Even Range
def even_range(start, end):
    even_list = []
    for i in range(start, end+1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

print(even_range(13, 20))
print(even_range(4, 11))
print(even_range(8, 5))

# Problems Completed [ ]

# Your test/solution code here 

def phrase_finder(words, phrase):
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] + " " + words[j] == phrase:
                return True
            elif words[j] + " " + words[i] == phrase:
                return True
    return False

print(phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye'))

# Problem 1

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "NaN"
    else:
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count

print(hamming_distance('abc', 'abc'))
print(hamming_distance('a1c', 'a2c'))
print(hamming_distance('!!!!', '****'))
print(hamming_distance('abc', 'ab'))


# Problem 2

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(29))
print(isPrime(200))

# Problem 3

def find_the_parity_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 1:
        return evens[0]
    else:
        return odds[0]

print(find_the_parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_the_parity_outlier([160, 3, 1719, 19, 11, 13, -21]))
