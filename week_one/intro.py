import time
from datetime import datetime, timedelta


my_int = 5

# Single line comment
# my_float = 2.67

#This is a bad comment
# This is a good comment

# Different strings
my_string = "mike"
my_string2 = 'mike'
my_string3 = """

mike

"""

# Quotes in a string
my_string4 = "Hello I am a 'car'"
my_string5 = 'Hello I am a "car"'

print(my_string4)
print(my_string5)



s1 = "Mike"
s2 = "Orrei"

concat_string = s1 + " " + s2
print(concat_string)

fstring = f"{s1} {s2}"
print(fstring)

print(f"Hello, my name is {s1} {s2}")


my_sum = 5 + 5
num2 = 5 - 3
num3 = 5 * 10
num4 = 16 / 8
num5 = 13 % 2

"""
Advanced Operators
x = 0
x += 1
x = x + 1

*=

exponent = **

5 ** 2

Comparison
>
<
>=
<=

Comparison
==

Assignment
=

!=

not

if x > 5 and y < 10

"""

# LIST
my_list = []
my_list2 = [1, 2, 3, 4, 5]
my_list3 = [["mike", "orrei"], ["jess", "williams"], ["matt", "wheeler"], ["melissa", "gwaldis"]]

print(my_list2)
print(my_list2[0])

print(my_list3[2][1])

# Dictionary
my_dict = {
    "1": "user1",
    "2": "user2",
    "3": "user3",
    "4": "user4",
    "5": "user5",
}

print(my_dict)
print(my_dict["3"])


my_nested = {
    "The Godfather": {
        "director": "Francis Ford Coppola",
        "released": 1972,
        "actors": ["Al Pacino", "Marlon Brando", "James Caan"],
    },
    "Fargo": {
        "director": "Joel and Ethan Coen",
        "released": 1996,
        "actors": ["William H. Macy", "Frances McDormand", "Steve Buscemi"],
    },
    "Blade Runner": {
        "director": "Ridley Scott",
        "released": 1982,
        "actors": ["Harrison Ford", "Rutger Hauer", "Daryl Hannah"],
    },
}

print(my_nested["The Godfather"]["released"])
print(my_nested["Blade Runner"]["actors"][2])

my_nested["The Godfather"]["released"] = 1930

print(my_nested["The Godfather"]["released"])

# If statements and conditionals
if my_nested["Fargo"]["released"] > 1990:
    print("This movie is not old")

if "director" in my_nested["The Godfather"]:
    print("This is true")

x = 5
y = 9

if x == 5 and y >= 10:
    print("Yes!")
else:
    print("No!")


a = 20

if a > 20:
    print("a is greater than 20")
elif a < 20:
    print("a is less than 20")
else:
    print("a is 20")


# Loops
b = 0

while b < 5:
    print(f"b is currently {b}")
    b += 1

for j in range(0, 5):
    print(f"j is currently {j}")


some_list = ['a', 'b', 'c', 'd', 'e', 'f']

for c in some_list:
    print(c)

for i in range(0, len(some_list)):
    print(some_list[i])

for i in my_dict:
    print(my_dict[i])



print("Enter your name!")
your_name = input()

print(f"Hello, {your_name}")

