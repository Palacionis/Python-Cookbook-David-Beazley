# Chapter two

# Problem_1 : You need to split a string but the delimiters are not consistent

# Solution : using re.split()

import re

line = "asdf fjdk; afed, fjek,asdf,       foo"
re.split(r"[;,\s]\s*", line)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# ---------------------------------------------------------------------------


# Problem_2 : You need to match text at the start or end of a string

# Solution : using str.startswith() and str.endswith()

filename = "soam.txt"
filename.endswith(".txt")
# True

# Providing multiple ends / starts

filenames = ["foo.c", "bar.py", "spam.c", "spam.h", "doc.txt"]
x = [name for name in filenames if name.endswith((".c", ".h"))]
print(x)
# ['foo.c', 'spam.c', 'spam.h']


# ---------------------------------------------------------------------------


# Problem_3 : Matching strings using shell wildcard patterns

# Solution : using fnmatch module

from fnmatch import fnmatch, fnmatchcase

addresses = [
    "5412 N CLARK ST",
    "1060 W ADDISON ST",
    "1039 W GRANVILLE AVE",
    "2122 N CLARK ST",
    "4802 N BROADWAY",
]

a = [addr for addr in addresses if fnmatch(addr, "* ST")]
print(a)
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']

b = [addr for addr in addresses if fnmatch(addr, "54[0-9][0-9] *CLARK*")]
print(b)
# ['5412 N CLARK ST']


# ---------------------------------------------------------------------------


# Problem_4 : Matching and searching for text patterns

# Solution : using re module


import re

text = "Today is 11/27/2012. PyCon starts 3/13/2013."

# (a) Find all matching dates
datepat = re.compile(r"\d+/\d+/\d+")
print(datepat.findall(text))
# ['11/27/2012', '3/13/2013']

# (b) Find all matching dates with capture groups
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
for month, day, year in datepat.findall(text):
    print("{}-{}-{}".format(year, month, day))
# 2012-11-27
# 2013-3-13


# (c) Iterative search
for m in datepat.finditer(text):
    print(m.groups())
# ('11', '27', '2012')
# ('3', '13', '2013')


# ---------------------------------------------------------------------------


# Problem_5 : Searching and replacing text

# Solution : using str.replace() and re.sub()

import re

text = "Today is 11/27/2012. PyCon starts 3/13/2013."

datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# (a) Simple substitution
print(datepat.sub(r"\3-\1-\2", text))
# Today is 2012-11-27. PyCon starts 2013-3-13.

# (b) Replacement function
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)}, {mon_name}, {m.group(3)}"


print(datepat.sub(change_date, text))
# Today is 27, Nov, 2012. PyCon starts 13, Mar, 2013.


# ---------------------------------------------------------------------------


# Problem_6 : Specifying a regexp for the shortest match

# Solution : adding '?' modifier afer '*' operator

import re

text = 'Computer says "no." Phone says "yes."'

# (a) Regex that finds quoted strings - longest match
str_pat = re.compile(r"\"(.*)\"")
print(str_pat.findall(text))
# ['no." Phone says "yes.']

# (b) Regex that finds quoted strings - shortest match
str_pat = re.compile(r"\"(.*?)\"")
print(str_pat.findall(text))
# ['no.', 'yes.']


# ---------------------------------------------------------------------------


# Problem_7 : Writing a regexp for multiple patterns

# Solution : using non-capture groups and re.DOTALL

import re

text = """/* this is a
              multiline comment */
"""

comment = re.compile(r"/\*((?:.|\n)*?)\*/")
print(comment.findall(text))
# [' this is a\n              multiline comment ']


# ---------------------------------------------------------------------------


# Problem_8 : Stripping unwanted characters from strings

# Solution : using strip() / lstrip() / rstrip()

text = "----hello===="
text.lstrip("-")
# 'hello===='

text.strip("-=")
# 'hello'


# ---------------------------------------------------------------------------


# Problem_9 : Sanitizing and cleaning up strings

# Solution : str.transalate()

s = "p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n"
print(s)
# pýtĥöñis	awesome

# (a) Remapping whitespace
remap = {ord("\t"): " ", ord("\f"): " ", ord("\r"): None}  # Deleted

a = s.translate(remap)
print("whitespace remapped:", a)
# whitespace remapped: pýtĥöñ is awesome

# (b) Remove all combining characters/marks
import unicodedata
import sys

cmb_chrs = dict.fromkeys(
    c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))
)

b = unicodedata.normalize("NFD", a)
c = b.translate(cmb_chrs)
print("accents removed:", c)
# accents removed: python is awesome

# (c) Accent removal using I/O decoding
d = b.encode("ascii", "ignore").decode("ascii")
print("accents removed via I/O:", d)
# accents removed via I/O: python is awesome


# ---------------------------------------------------------------------------


# Problem_9 : Combining and concatenating strings

# Solution : using .join() that accepts an iterable


def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


# (a) Simple join operator
text = "".join(sample())
print(text)

# (b) Redirection of parts to I/O
import sys

for part in sample():
    sys.stdout.write(part)
sys.stdout.write("\n")
# IsChicagoNotChicago?

# (c) Combination of parts into buffers and larger I/O operations
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield "".join(parts)
            parts = []
            size = 0
    yield "".join(parts)


for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write("\n")
# IsChicagoNotChicago?
