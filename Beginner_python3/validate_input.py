# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("12 chars max")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Username cannot contain digits")
else:
    print(f"Welcome {username}")
