# Accessing and Modifying Data:
# 1. The traditional way: make the data private and use getters and setters:

class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user._username}: Hi {user._username}, it is {self._username}")



def main():
    u1 = User("DAN", "dan@gmail.com", "123")
    u2 = User("bat", "bat@gmail.com", "abc")
    u1.say_hi_to_user(u2)

if __name__ == "__main__":
    main()
