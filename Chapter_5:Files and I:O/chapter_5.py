# Chapter five


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


# ---------------------------------------------------------------------------


# Problem_4 : iterating over fixed-sized records

# Solution : using iter function anf functools.partial() method 

from functools import partial
RECORD_SIZE = 32

with open('data.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)


# ---------------------------------------------------------------------------


# Problem_5 : getting directory listing

# Solution : using os and glob modules



import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for r in name_sz_date:
    print(r)

# Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)