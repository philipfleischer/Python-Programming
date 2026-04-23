# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.2f}")  # $3.14
print(f"Price 2 is ${price2:.2f}")  # $-987.65
print(f"Price 3 is ${price3:.2f}")  # $12.34

print(f"Price 1 is ${price1:.1f}")  # $3.1
print(f"Price 2 is ${price2:.1f}")  # $-987.6
print(f"Price 3 is ${price3:.1f}")  # $12.3

print(f"Price 1 is ${price1:.3f}")  # $3.142
print(f"Price 2 is ${price2:.3f}")  # $-987.650
print(f"Price 3 is ${price3:.3f}")  # $12.340

# Here we add ' ' so that the whole string is 10 chars in length:
print(f"Price 1 is ${price1:10}")  # $          3.14159
print(f"Price 2 is ${price2:10}")  # $          -987.65
print(f"Price 3 is ${price3:10}")  # $          12.34

# Here we add '0' so that the whole string is 10 chars in length:
print(f"Price 1 is ${price1:010}")  # $0003.14159
print(f"Price 2 is ${price2:010}")  # $-000987.65
print(f"Price 3 is ${price3:010}")  # $0000012.34

# Here we left justify them with :> so that space comes at left side:
print(f"Price 1 is ${price1:<10}")  # $3.14259
print(f"Price 2 is ${price2:<10}")  # $-987.65
print(f"Price 3 is ${price3:<10}")  # $12.34

# DEFAULT:
# Here we right justify them with :< so that space comes at right side:
print(f"Price 1 is ${price1:>10}")  # $   3.14259
print(f"Price 2 is ${price2:>10}")  # $   -987.65
print(f"Price 3 is ${price3:>10}")  # $     12.34

# Here we center justify them with :^
print(f"Price 1 is ${price1:^10}")  # $ 3.14259
print(f"Price 2 is ${price2:^10}")  # $ -987.65
print(f"Price 3 is ${price3:^10}")  # $  12.34

# Here we precede values with +/- operators:
print(f"Price 1 is ${price1:+}")  # $+3.14259
print(f"Price 2 is ${price2:+}")  # $-987.65
print(f"Price 3 is ${price3:+}")  # $+12.34

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34
# Here we Thousands separate them
print(f"Price 1 is ${price1:,}")  # $3,000.14259
print(f"Price 2 is ${price2:,}")  # $-9,870.65
print(f"Price 3 is ${price3:,}")  # $1,200.34

# Here we combine them!
print(f"Price 1 is ${price1:+,.2f}")  # $+3,000.14
print(f"Price 2 is ${price2:+,.2f}")  # $-9,870.65
print(f"Price 3 is ${price3:+,.2f}")  # $+1,200.34
