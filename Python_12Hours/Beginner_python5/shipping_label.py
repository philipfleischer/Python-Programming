def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for value in kwargs.values():
        print(value, end=" ")
    print()
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# This is a combination of positional arguments first,
# and then keyword arguments later, which will get
# put in the two different containers in the
# shipping_label(*args, **kwargs) tuple and dict
shipping_label("Dr.", "Philip", "Fleischer", "III",
               street="Eddaveien 13L",
               apt="#28",
               city="Jeløya",
               state="Moss",
               zip="1513")
# OUTPUT:
# Dr. Philip Fleischer III
# Eddaveien 13L #28 Jeløya Moss 1513

# Eddaveien 13L #28
# Jeløya Moss 1513

print()
print()

shipping_label(
    "Dr.","Philip","Fleischer","III",
    street="Eddaveien 13L",
    pobox="PO box #1001",
    city="Jeløya",
    state="Moss",
    zip="1513",
)
# OUTPUT:
# Dr. Philip Fleischer III
# Eddaveien 13L PO box #1001 Jeløya Moss 1513

# Eddaveien 13L
# PO box #1001
# Jeløya Moss 1513
