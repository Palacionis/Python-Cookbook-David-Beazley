# Chapter seven - Functions

# Problem_1 : writing functions that accept any number of arguments

# Solution : using * argument


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


avg(1, 2)  # 1.5
avg(1, 2, 3, 4)  # 2.5


# ---------------------------------------------------------------------------


# Problem_2 : writing functions that accept any number of keyword arguments

# Solution : using ** argument


def fn(**kwargs):
    keyvalues = [x for x in kwargs]
    for x in keyvalues:
        print(kwargs[x])


fn(a="One", b="Two", c="Three")
# One
# Two
# Three

# A * argument can only appear as the last positional argument in a function definition
# A ** argument can only appear as the last argument. A subtle aspect of function definitions is that arguments can still appear after a * argument.


def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass


# ---------------------------------------------------------------------------


# Problem_3 : writing functions that only accept keyword arguments

# Solution : placing keyword arguments after a * argument


def recv(maxsize, *, block):
    print("Function works")
    pass


recv(1024, True)  # TypeError
recv(1024, block=True)  # Function works


# using this technique with functions that accept a varying number of positional arguments:


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minimum(1, 2, 5, -5, 10)  # returns -5
minimum(1, 2, 5, -5, 10, clip=0)  # returns 0


# ---------------------------------------------------------------------------


# Problem_4 : you want to attach additional information to your function

# Solution : using function argument annotations, it does not attach any semantic meaning
"""
def add(x:int, y:int) -> int:
    return x+y

add(1,6) # returns 7
"""

# ---------------------------------------------------------------------------


# Problem_5 : writing a function that returns multiple values

# Solution : returning a tuple of values


def fn():
    return 1, 2, 3


a, b, c = fn()
a  # 1
b  # 2
c  # 3


# ---------------------------------------------------------------------------


# Problem_6 : defining functions with default arguments

# Solution : assign values in the function definition, make sure that default arguments appear last


def spam(a, b=42):
    print(a, b)


spam(1)  # a=1, b=42
spam(1, 2)  # a=1, b=2

# If the default value is a mutable container, use None and define it inside the function


def spam(a, b=None):
    if b is None:
        b = []
        ...


# remember that default values are bound only once at the time of the function definition

x = 42


def spam(a, b=x):
    print(a, b)


spam(1)  # 1, 42

x = 23  # has no effect

spam(1)  # 1, 42


# ---------------------------------------------------------------------------


# Problem_7 : defining anonymous or inline functions

# Solution : using lambda

add = lambda x, y: x + y
a = add(1, 2)
a  # 3


# ---------------------------------------------------------------------------


# Problem_8 : capturing variables in anonymous functions

# Solution : using x=x inside lambda

# for example

x = 10
a = lambda y: y + x
x = 20
b = lambda y: y + x


a(10)  # returns 30 instead of 20
b(10)  # returns 30

x = 15
a(10)  # returns 25

x = 3
a(10)  # returns 13

# if you want an anonymous function to capture a value at the point of definition nad keep it:

x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

a(10)  # returns 20
b(10)  # returns 30


# ---------------------------------------------------------------------------


# Problem_9 : making an n-argument callable work with fewer arguments

# Solution : functools.partial

# Calculating distance from a point in to all the other poitns and returning the list sorted

import functools

points = [(1, 2), (3, 4), (5, 6), (7, 7)]

import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=functools.partial(distance, pt))
print(points)