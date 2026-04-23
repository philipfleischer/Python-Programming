# for loops = execute a block of code a fixed number of times.
#               You can iterate over a range, string, sequence, etc.

# Print 1-10
for i in range(1, 11):
    print(i)

# print 10-1
for i in reversed(range(1, 11)):
    print(i)

# print Hello World! char for char
sentence = "Hello World!"
for word in sentence:
    for char in word:
        print(char)

# print Hello World! char for char, but reversed
sentence = "Hello World!"
for word in reversed(sentence):
    for char in word:
        print(char)

# print "HEllo World!" reversed
for word in reversed(sentence):
    print(word)

# print annenhvert tall
for i in range(1, 11, 2):
    print(i)


credit_card = "1234-2131-2122-2131"
for i in credit_card:
    # We do not print '-', and jump over it
    if i == "-":
        continue
    else:
        print(i)
