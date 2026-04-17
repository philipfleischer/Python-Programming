# Should use tuple when we can, since it is ordered
# and unchangeable, making it much faster and efficient

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# OUTPUT:
# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #
