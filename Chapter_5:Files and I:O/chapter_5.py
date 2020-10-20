# Chapter four


# Problem_1 : you need to write text data in different text encodings suchs as ASCII

# Solution : using open() with more rt to read a text file

with open("somefile.txt", "rt") as f:
    data = f.read()


# ---------------------------------------------------------------------------


# Problem_2 : you need to redirect the print output to a a file

# Solution : using file keyword in print method

with open("somefile.txt", "wt") as f:
    print("hello world", file=f)


# ---------------------------------------------------------------------------


# Problem_3 : reading and writing binary data

# Solution : using rb parameter in open

with open("somefile.txt", "rb") as f:  # 'wb' to write
    data = f.read()


# ---------------------------------------------------------------------------


# Problem_3 : reading and writing compressed datafiles

# Solution : using gzip and bz2 modules

import gzip
with gzip.open('somefile.gz', 'rt') as f: # wt to write
    text = f.read()

import bz2
with bz2.open('somefile.gz', 'rt') as f:
    text = f.read()
