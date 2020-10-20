# Chapter three

# ---------------------------------------------------------------------------


# Problem_1 : Performing accurate calculations with decimal numbers

# Solution : using decimals module

a = 4.2
b = 2.1
print(a + b)
# 6.3000000000000001

(a + b) == 6.3
# False

from decimal import Decimal

a = Decimal("4.2")
b = Decimal("2.1")
print(a + b)
Decimal("6.3")
(a + b) == Decimal("6.3")
# True


# ---------------------------------------------------------------------------


# Problem_2 : converting integers to binary, octal or hexadecimal digits

# Solution : using built in bin(), hex() and oct()

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

# 0b10011010010
# 0o2322
# 0x4d2


# ---------------------------------------------------------------------------


# Problem_3 : getting the last friday date

# Solution : datetime module


from datetime import datetime, timedelta

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


# ---------------------------------------------------------------------------


# Problem_4 : converting strings into datetimes

# Solution : datetime module

from datetime import datetime

text = "2020-07-14"
y = datetime.strptime(text, "%Y-%m-%d")
z = datetime.now()
diff = z - y
print(diff)

# 96 days, 14:16:23.718860
