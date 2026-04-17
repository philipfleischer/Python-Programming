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

values = capitals.values()
for value in capital.values:
    print(value)
