# Question 51 — Type Casting Output

a = "50"
b = int(a)

print(a)
print(b)
print(type(a))
print(type(b))

# Output:
# 50
# 50
# <class 'str'>
# <class 'int'>


# Question 52 — Float to Integer

number = 99.99
result = int(number)

print(number)
print(result)

# Output:
# 99.99
# 99
# Explanation: Casting a float to int truncates (discards) the decimal portion without rounding.


# Question 53 — Arithmetic Output

a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# Output:
# 17
# 7
# 60
# 2.4
# 2
# 2


# Question 54 — Parentheses Challenge

print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))

# Output:
# 20
# 30
# 7.0
# 2.5
# Explanation: Parentheses override standard operator precedence, evaluating operations inside them first.


# Question 55 — Digit Challenge

number = 684

a = number % 10
b = number // 10
c = b % 10
d = number // 100

print(a)
print(c)
print(d)

# Output:
# 4
# 8
# 6
# Variable Identification:
# a = Ones digit (4)
# c = Tens digit (8)
# d = Hundreds digit (6)