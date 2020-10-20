# Chapter six

# Problem_1 : you need to write text data in different text encodings suchs as ASCII

# Solution : using open() with more rt to read a text file

with open("somefile.txt", "rt") as f:
    data = f.read()


# ---------------------------------------------------------------------------
