# Chapter  eighth - Classes and Objects

# Problem_8 : changing a the string represantation of instances

# Solution : using __str__() and __repr__()


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Pair({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Pair(1, 2)

a  # Pair(1,2) - __repr__() output
print(a)  # (1,2) - __str__() output

# ---------------------------------------------------------------------------
