# 1. Get Name
def get_name():
    name = input("What is your name? ")
    return name
2. Say Hello
name = get_name()
print(f"Hello, {name}!")

# 2.  Reverse It

def reverse_it():
    string = "a man, a plan, a canal, frenemies!"
    reverse = ""

    for i in range(len(string)):
        reverse += string[len(string) - (i + 1)]

    print(reverse)

# Reverse
reverse_it()

# 3. Swap Em

def swap_em():
    a = 10
    b = 30

    temp = b
    b = a
    a = temp

    print(f"a is now {a}, and b is now {b}")

# Swap
swap_em()

# 4. Multiply Array/List

def multiply_array(ary):
    if len(ary) == 0:
        return 1

    total = 1

    for num in ary:
        total *= num

    return total

# Array
numbers = [1, 2, 3, 4]
result = multiply_array(numbers)
print(f"The product of the array is: {result}")

# 5. Fizz Buzzer

def fizzbuzzer(x):
    if x % (3 * 5) == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 0:
        return 'buzz'
    else:
        return 'archer'

# fizzbuzz
number = 15
result = fizzbuzzer(number)
print(f"The result for {number} is: {result}")

# 6. Nth Fibonacci

def nth_fibonacci_number():
    fibs = [1, 1]
    num = int(input("Which Fibonacci number do you want? "))

    while len(fibs) < num:
        next_fib = fibs[-2] + fibs[-1]
        fibs.append(next_fib)

    print(f"{fibs[-1]} is the Fibonacci number at position {num}")

# fibonacci number 
nth_fibonacci_number()

# 7. Search Array/List

def search_array(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return True
    return False

# Search Array
array = [1, 2, 3, 4, 5]
value = 3
result = search_array(array, value)
print(f"Is {value} present in the array? {result}")

# 8. Palindrome

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

# Palindrome
string = "racecar"
result = is_palindrome(string)
print(f"Is '{string}' a palindrome? {result}")

# 9. hasDupes

def has_dupes(arr):
    seen = {}
    for item in arr:
        if item in seen:
            return True
        else:
            seen[item] = True
    return False

# duplicates
array = [1, 2, 3, 4, 5, 3]
result = has_dupes(array)
print(f"Does the array have duplicates? {result}")
