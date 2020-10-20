# Chapter four


# Problem_1 : you need to process items in an iterable but dont want to use a for loop

# Solution : using next() and catching StopIteration execption

with open("/folder/passwd") as f:
    try:
        while True:
            line = next(f)
            print(line, end="")
    except StopIteration:
        pass


# ---------------------------------------------------------------------------


# Problem_2 : delegating an iteration

# Solution : simply define __iter__() method


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
    print(ch)
# Node(1), Node(2)


# ---------------------------------------------------------------------------


# Problem_3 : creating new iteration patterns with generators

# Solution : define a generator function


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 2, 0.5):
    print(n)

# 0
# 0.5
# 1.0
# 1.5


# ---------------------------------------------------------------------------


# Problem_3 : add iteration protocol to an custom object

# Solution : using __iter__()


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f"Node {self._value}"

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Example
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))

for ch in root.depth_first():
    print(ch)

# Node(0)
# Node(1)
# Node(3)
# Node(4)
# Node(2)
# Node(5)


# ---------------------------------------------------------------------------


# Problem_4 : iterating in vreverse

# Solution : using built-ind reversed()

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)
# 4
# 3
# 2
# 1

# Another example


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


c = Countdown(5)
print("Forward:")
for x in c:
    print(x)
# Forward:
# 5
# 4
# 3
# 2
# 1

print("Reverse:")
for x in reversed(c):
    print(x)
# Reverse:
# 1
# 2
# 3
# 4
# 5


# ---------------------------------------------------------------------------


# Problem_5 : taking slice of an iterator

# Solution : using itertools.islice() method


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
c[10:20]
# TypeError: 'generator' object is not subscriptable

import itertools

for x in itertools.islice(c, 10, 15):
    print(x)
# 10
# 11
# 12
# 13
# 14


# ---------------------------------------------------------------------------


# Problem_5 : skipping the first part of an iterable

# Solution : using itertools.dropwhile() method

from itertools import dropwhile

with open("/folder/passwd") as f:
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line, end="")
        # removes the first lines that start with an #
        # once dropwhile meets a False it stops and the following lines with #
        # will not be dropped


# ---------------------------------------------------------------------------


# Problem_6 : iterating over all possible combinations or permutations

# Solution : using itertools.permutations method


from itertools import permutations

items = ["a", "b", "c"]
for p in permutations(items):  # can accept argument of how many items to include
    print(p)
# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')

for p in permutations(items, 2):  # can accept argument of how many items to include
    print(p)
# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')

# itertools.combinations() does not take the index of an item in consideration

items = ["a", "b", "c"]
from itertools import combinations

for p in combinations(items, 3):
    print(p)
# ('a', 'b', 'c')


for p in combinations(items, 2):
    print(p)
# ('a', 'b')
# ('a', 'c')
# ('b', 'c')

from itertools import combinations_with_replacement

for p in combinations_with_replacement(items, 3):
    print(p)
# ('a', 'a', 'a')
# ('a', 'a', 'b')
# ('a', 'a', 'c')
# ('a', 'b', 'b')
# ('a', 'b', 'c')
# ('a', 'c', 'c')
# ('b', 'b', 'b')
# ('b', 'b', 'c')
# ('b', 'c', 'c')
# ('c', 'c', 'c')


# ---------------------------------------------------------------------------


# Problem_7 : iterating over the index-value pairs of a sequence

# Solution : using enumerate() method

my_list = ["a", "b", "c"]

for idx, val in enumerate(my_list):
    print(idx, val)
# 0 a
# 1 b
# 2 c


# ---------------------------------------------------------------------------


# Problem_8 : iterating over multiple sequences simultaneously

# Solution : using zip() method

xpts = [1, 5, 4, 2, 10]
ypts = [101, 25, 243, 63, 1]

for x, y in zip(xpts, ypts):
    print(x, y)
# 1 101
# 5 25
# 4 243
# 2 63
# 10 1


# ---------------------------------------------------------------------------


# Problem_9 : iterating on items in separate containers

# Solution : using itertools.chain() method

from itertools import chain

a = [1, 2, 3, 4]
b = ["x", "y", "z"]
for x in chain(a, b):
    print(x)
# 1
# 2
# 3
# 4
# x
# y
# z


# ---------------------------------------------------------------------------


# Problem_10 : flattening a nested sequence

# Solution : using recursive generator function involving a yield from statement

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x, ignore_types)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
items_flattened = list(flatten(items))
print(items_flattened)
# [1, 2, 3, 4, 5, 6, 7, 8]


# ---------------------------------------------------------------------------


# Problem_11 : iterating in sorted order over merged sorted iterables

# Solution : using heapq.merge() method

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
# important note that heapq.merge() requires altready sorted iterables
for c in heapq.merge(a, b):
    print(c)
# 1
# 2
# 4
# 5
# 6
# 7
# 10
# 11

