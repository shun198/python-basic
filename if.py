age = 16
graduate_highschool = 18

if age >= graduate_highschool:
    print("You can graduate highschool")
elif age >= 15:
    print("You can't graduate highschool yet")
else:
    print("You can't enter highschool")
age = 11
if not 15 < age < 18:
    print("You can't enter highschool")

a = None
if a:
    print("a is None")
else:
    print("a is not None")

if not a:
    print("a is None")
else:
    print("a is not None")
