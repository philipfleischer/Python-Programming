class Math:

    # Not changing method,
    # they do not change anything since they do not have access to anything, it only acts as a function
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")


def main():
    print(Math.add5(5))
    print(Math.add10(10))
    Math.pr()

if __name__ == "__main__":
    main()
