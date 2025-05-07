import math

def basic_math(a, b,):
    sum = a + b
    diff = a - b
    prod = a * b
    quot = a / b
    mod = a % b

    return (sum, diff, prod, quot, mod)

print(basic_math(12, 5))

def circle_metrics(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return (area, circumference)

print(circle_metrics(7))

def power_and_root(x, n):
    power = x ** n
    root = x ** (1/n)

    return (power, root)

print(power_and_root(27, 3))

def bits_to_gigabytes(bits):
    return bits / (8 * 1024 ** 3) # Convert bits to gigabytes

print(bits_to_gigabytes(8589934592)) # 8 GB in bits

def rounding_ops(num):
    floor = math.floor(num)
    ceil = math.ceil(num)
    round_num = round(num)

    return (floor, ceil, round_num)

print(rounding_ops(3.14159))     # Output: (3, 4, 3.14)
print(rounding_ops(9.87654321))  # Output: (9, 10, 9.88)


def hypotenuse(a, b):
    return math.hypot(a, b)

print(hypotenuse(3, 4))   # Output: 5.0
print(hypotenuse(5, 12))  # Output: 13.0


