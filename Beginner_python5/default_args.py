# default arguments = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

# We could send in this ($500, 0 discount and 5% salestax).
# But not very user friendly and also, they might not
# change all that often, making them a pain to write each time.
print(f"net_price(500, 0, 0.05) = ${net_price(500, 0, 0.05)}")

# Since we set default values above, we can just write it like this:
print(f"net_price(500) = ${net_price(500)}")
# 10% discount instead of default of 0:
print(f"net_price(500, 0.1) = ${net_price(500, 0.1)}")
# as well as 10% tax:
print(f"net_price(500, 0.1, 0.1) = ${net_price(500, 0.1, 0.1):.2f}")

# OUTPUT:
# net_price(500, 0, 0.05) = $525.0
# net_price(500) = $525.0
# net_price(500, 0.1) = $472.5
# net_price(500, 0.1, 0.1) = $495.00

import time

# start=0 needs to be after any NON-default arguments
def count(end, start=0):
    for i in range(start, end+1):
        print(i)
        time.sleep(1)
    print("DONE!")

count(10, 5)
