# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}

print(f"capitals.get('USA') = {capitals.get('USA')}")
print(f"capitals.get('India') = {capitals.get('India')}")
print(f"capitals.get('Japan') = {capitals.get('Japan')}")
print()

if capitals.get("Japan"):
    print(f"capitals.get('Japan') = {capitals.get('Japan')}")
else:
    print("That capital does not exist in codebase.")
print()

capitals.update({"Germany": "Berlin"})
print(capitals)
print()
capitals.update({"USA": "Venezuela?"})
print(capitals)
print()
capitals.pop("China")
print(capitals)
print()
# Removes the latest key:value pair
capitals.popitem()
print(capitals)
print()
capitals.clear()
print(capitals)
print()

capitals = {
    "USA": "Washington D.C.",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow",
}

keys = capitals.keys()
print(f"print(keys) = {keys}")
print()

for key in capitals.keys():
    print(f"Print for key in capitals.key() = {key}")
print()

for values in capitals.values():
    print(f"Print values in capitals.values() = {values}")
print()

print("Capital values:")
values = capitals.values()
for value in capitals.values():
    print(value)
print()

print("Capital items:")
items = capitals.items()    # items =  [(), (), ...]
print(items)
print()

for key, value in capitals.items():
    print(f"{key} : {value}")
print()

# OUTPUT:
# capitals.get('USA') = Washington D.C.
# capitals.get('India') = New Dehli
# capitals.get('Japan') = None

# That capital does not exist in codebase.

# {'USA': 'Washington D.C.', 'India': 'New Dehli', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# {'USA': 'Venezuela?', 'India': 'New Dehli', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# {'USA': 'Venezuela?', 'India': 'New Dehli', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# {'USA': 'Venezuela?', 'India': 'New Dehli', 'Russia': 'Moscow'}

# {}

# print(keys) = dict_keys(['USA', 'India', 'China', 'Russia'])

# Print for key in capitals.key() = USA
# Print for key in capitals.key() = India
# Print for key in capitals.key() = China
# Print for key in capitals.key() = Russia

# Print values in capitals.values() = Washington D.C.
# Print values in capitals.values() = New Dehli
# Print values in capitals.values() = Beijing
# Print values in capitals.values() = Moscow

# Capital values:
# Washington D.C.
# New Dehli
# Beijing
# Moscow

# Capital items:
# dict_items([('USA', 'Washington D.C.'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

# USA : Washington D.C.
# India : New Dehli
# China : Beijing
# Russia : Moscow
