# Chapter one

# Problem_1 : unpack N elements from an iterable, but the iterable may be longer than N elements causing 'too many values to unpack' exception

# Solution : using star expressions


# Taking only the middle grades
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


grades = [10, 9, 9, 8, 7, 10]

drop_first_last(grades)
# 8.25

# Taking only the numbers that are the last elements in an iterable
record = ("Dave", "dave@gmail.com", "861836885", "43235614", "342362145")
name, email, *phone_numbers = record
# ['861836885', '43235614', '342362145']


# ---------------------------------------------------------------------------


# Problem_2 :  keeping the last N items during some kind of process, here is an example of only having 5 lines at a time from a text file

# Solution : using deque


from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open("test_2.txt") as f:
    for line, prevlines in search(f, "python", 4):
        for pline in prevlines:
            print(pline, end="")
        print(line, end="")


# ---------------------------------------------------------------------------


# Problem_3 : finding the largest or smallest N items from an iterable

# Solution : nlargest() and nsmallest() from heapq

import heapq
import random

nums = [random.randint(x, 100) for x in range(15)]
print(heapq.nlargest(3, nums))
# [100, 88, 82]
print(heapq.nsmallest(3, nums))
# [28, 30, 37]


# ---------------------------------------------------------------------------


# Problem_4 : finding the largest and smalles value from a dict

# Solution : using zip() to swap keys with values


prices = {"ACME": 45.23, "APPL": 654.32, "IBM": 34.56, "FB": 142.24}

min_price = min(zip(prices.values(), prices.keys()))
# (34.56, 'IBM')

max_price = max(zip(prices.values(), prices.keys()))
# (654.32, 'APPL')


# ---------------------------------------------------------------------------


# Problem_5 : sorting the dict by values:

# Solution : using sorted with zip


prices = {"ACME": 45.23, "APPL": 654.32, "IBM": 34.56, "FB": 142.24}

prices_sorted = sorted(zip(prices.values(), prices.keys()), reverse=True)
# [(654.32, 'APPL'), (142.24, 'FB'), (45.23, 'ACME'), (34.56, 'IBM')]


# ---------------------------------------------------------------------------


# Problem_6 : getting the key of the smallest or highest value

# Solution : lambda


prices = {"ACME": 45.23, "APPL": 654.32, "IBM": 34.56, "FB": 142.24}

print(f"The key of the max value is {max(prices, key=lambda k: prices[k])}")
print(f"The key of the min value is {min(prices, key=lambda k: prices[k])}")
# The key of the max value is APPL
# The key of the min value is IBM


# ---------------------------------------------------------------------------


# Problem_7 : finding whats common between two dictionaries

# Solution : using sets

a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}

# finding common keys
a.keys() & b.keys()
# {'x', 'y'}

# finding keys in a that are not in b
a.keys() - b.keys()
# {'z'}

# finding key,value pairs in common
a.items() & b.items()
# {('y', 2)}


# ---------------------------------------------------------------------------


# Problem_8 : eliminating duplicates while maintaining order

# Solution : for loop and set


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10, 5]
list(dedupe(a))
# [1, 5, 2, 9, 10]

# for unhashable items


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 2}, {"x": 2, "y": 4}]

list(dedupe(a, key=lambda d: (d["x"], d["y"])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]


# ---------------------------------------------------------------------------


# Problem_9 : determining the most frequently occuring items in a sequence

# Solution : collections.Counter comes with a most_common() method

words = [
    "look",
    "into",
    "my",
    "eyes",
    "look",
    "into",
    "my",
    "eyes",
    "eyes",
    "eyes",
    "my",
]

from collections import Counter

word_counts = Counter(words)
top_3 = word_counts.most_common(3)
# [('eyes', 4), ('my', 3), ('look', 2)]


# ---------------------------------------------------------------------------


# Problem_10 : sorting a list of dictionaries by a common key

# Solution : using itemgetter function from the operator module


from operator import itemgetter

rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
]

rows_by_fname = sorted(rows, key=itemgetter("fname"))
# [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]

rows_by_uid = sorted(rows, key=itemgetter("uid"))
# [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#  {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#  {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

# itemgetter also accepts mutiple keys

rows_by_lfname = sorted(rows, key=itemgetter("lname", "fname"))
# [{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#  {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#  {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
#  {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]


# ---------------------------------------------------------------------------


# Problem_11 : grouping records togetger based on a field

# Solution : using itertools.groupby() function

rows = [
    {"address": "5412 N CLARK", "date": "07/01/2012"},
    {"address": "5148 N CLARK", "date": "07/04/2012"},
    {"address": "5800 E 58TH", "date": "07/02/2012"},
    {"address": "5645 N RAVENSWOOD", "date": "07/03/2012"},
    {"address": "5645 N RAVENSWOOD", "date": "07/02/2012"},
    {"address": "1060 W ADDISON", "date": "07/02/2012"},
    {"address": "4801 N BROADWAY", "date": "07/01/2012"},
    {"address": "1039 W GRANVILLE", "date": "07/04/2012"},
]

from operator import itemgetter
from itertools import groupby

# sort by the desired field first
rows.sort(key=itemgetter("date"))

# iterate in groups
for date, items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print("   ", i)

# 07/01/2012
#     {'address': '5412 N CLARK', 'date': '07/01/2012'}
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
# 07/02/2012
#     {'address': '5800 E 58TH', 'date': '07/02/2012'}
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'}
# 07/03/2012
#     {'address': '5645 N RAVENSWOOD', 'date': '07/03/2012'}
# 07/04/2012
#     {'address': '5148 N CLARK', 'date': '07/04/2012'}
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}


# ---------------------------------------------------------------------------


# Problem_12 : filtering sequence elements

# Solution : using comprehensions or generator expressions

my_list = [1, -4, 5, 7, 10, 15, -5, 9]
res = [x for x in my_list if x > 0]

# [1, 5, 7, 10, 15, 9]
# the dowside of a compregension is that it will procuduce a large result if the input is large

pos = (n for n in my_list if n > 0)
# <generator object <genexpr> at 0x10b0aa250>

for x in pos:
    print(x)

# 1
# 5
# 7
# 10
# 15
# 9

# filtering sequences that are a bit trickier, but it can be achieved with filter function

values = ["2", "1", 2, None, 5, "5", ["1", 2]]


def is_int(val):
    try:
        x = int(val)
        return True
    except:
        return False


int_vals = list(filter(is_int, values))
# ['2', '1', 2, 5, '5']

# or using a list comprehension
int_vals = [x for x in values if is_int(x)]

# if we want to replace the values that does not meet our criteria we move the filter criterion into a conditional expression
int_vals_replaced = [x if is_int(x) else 0 for x in values]
# ['2', '1', 2, 0, 5, '5', 0]


# ---------------------------------------------------------------------------


# Problem_14 : filtering two sequence elements with one condition. Suppose you want to filter the address list where the item in list count is more than 5

# Solution : using itertools.compress


addresses = [
    "5412 N CLARK",
    "5148 N CLARK",
    "5800 E 58TH",
    "2122 N CLARK",
    "5645 N RAVENSWOOD",
    "1060 W ADDISON",
    "4801 N BROADWAY",
    "1039 W GRANVILLE",
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
# [False, False, True, False, False, True, True, False]

list(compress(addresses, more5))
# ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']


# ---------------------------------------------------------------------------


# Problem_15 : selecting a subset of a dictionary

# Solution : dictionary comprehensions

prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20, "FB": 10.75}

# making a dict of prices over 150$
p1 = {key: value for key, value in prices.items() if value > 150}
# {'AAPL': 612.78, 'IBM': 205.55}

# by filtering keys
tech_names = {"ACME", "AAPL", "IBM"}
p2 = {key: value for key, value in prices.items() if key in tech_names}
# {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}


# ---------------------------------------------------------------------------


# Problem_16 : access sequence elements by name rather than index

# Solution : namedtuple from collections module

from collections import namedtuple

Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jones@gmail.com", "2020-05-04")
# Subscriber(addr='jones@gmail.com', joined='2020-05-04')

sub.addr
# 'jones@gmail.com'

sub.joined
# '2020-05-04'

# ---------------------------------------------------------------------------


# Problem_17 : transform and recude data at the same time

# Solution : generator-expression argument

# calculating the sum of the squares
s = sum(x * x for x in range(1, 11))
# 385

# Data reduction across fields of a data structure
portfolio = [
    {"name": "GOOG", "shares": 50},
    {"name": "YHOO", "shares": 75},
    {"name": "AOL", "shares": 20},
    {"name": "SCOX", "shares": 65},
]

min_shares = min(s["shares"] for s in portfolio)
# 20

min_shares_2 = min(portfolio, key=lambda s: s["shares"])
# {'name': 'AOL', 'shares': 20}
