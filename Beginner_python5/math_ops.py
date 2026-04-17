# function = A block of reusable code
#              place () after the function name to invoke it

def happy_birtday(name: str, age: int):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birtday("Philip", 21)
happy_birtday("Elias", 22)
happy_birtday("Fleischer", 23)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("PHLILPEF", 42.50, "01/01")


# return = statement used to end a function
#            and send a result back to the caller

def add(x, y):
    z = x + y
    return z


def sub(x, y):
    z = x - y
    return z


def mul(x, y):
    z = x * y
    return z


def div(x, y):
    z = x / y
    return z

print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))
