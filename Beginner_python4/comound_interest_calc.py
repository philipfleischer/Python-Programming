# Pytho compound interest calculator

principle, rate, time = 0, 0, 0

while principle <= 0:
    principle = float(input("Enter principle: "))
    if principle <= 0:
        print("Principle cant be less than or equal to 0")

print(principle)

while rate <= 0:
    rate = float(input("Enter rate: "))
    if rate <= 0:
        print("rate cant be less than or equal to 0")

print(rate)


while time <= 0:
    time = int(input("Enter time: "))
    if time <= 0:
        print("time cant be less than or equal to 0")

print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")


# If the conditions in the while is not true, then we skip the
# while loops, but we might not want that or it might be untrue,
# and we still want to enter, so we can use while True:
while True:
    age = int(input("What age can you drive a car?: "))
    if age < 18:
        print("Nope")
    else:
        break
