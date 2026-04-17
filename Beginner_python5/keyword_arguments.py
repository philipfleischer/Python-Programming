# keyword arguments = an argument preceded by an identifier
#                       helps with readability
#                       order of arguments does not matter
#                       1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "MR.", "Philip", "Fleischer")
# OUT -> Hello MR. Philip Fleischer
hello("Hello", "Duck", "Donald", "DR.")
# OUT -> Hello Duck Donald DR.
# Med keyword arguments så spiller ikke rekekfølgen på
# argumentene MED keyword noen rolle, men det gjør fortsatt
# det for de uten:
hello("Hello", last="Duck", first="Donald", title="DR.")
# OUT -> Hello DR. Donald Duck
hello("DR.", "Hello", last="Duck", first="Donald")
# OUT -> DR. Hello Donald Duck
hello(title="DR.", greeting="Hello", last="Duck", first="Donald")
# OUT -> Hello DR. Donald Duck

# helt korrekt:
hello(greeting="Hello", title="DR.", first="Donald", last="Duck")
# OUT -> Hello DR. Donald Duck

for i in range(1, 11):
    print(i, end=" ") # end er keyword arg
# OUT -> 1 2 3 4 5 6 7 8 9 10
print()

print("1", "2", "3", "4", "5", sep="---")
# OUT -> 1---2---3---4---5
