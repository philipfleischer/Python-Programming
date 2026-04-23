import math

x = 3.14
y = -4
z = 5

result = round(x)

print(f"{x} rounded = {result}")

result = abs(y)
print(f"absolute value of: {y} = {result}")

exponent = 3
result = pow(z, exponent) # 5^3
print(f"{z} to the power of {exponent} = {result}")

result = max(x, y, z)
print(f"The max value of {x, y, z} = {result}")

result = min(x, y, z)
print(f"The min value of {x, y, z} = {result}")

print(f"The math.pi call gives = {math.pi}")
print(f"The exponential constant math.e = {math.e}")

result = math.sqrt(z)
print(f"The math.sqrt({z}) = {result}")

result = math.ceil(x)
print(f"The math.ceil function rounds up, math.ceil({x}) = {result}")

result = math.floor(x)
print(f"The math.floor({x}) function = {result}")
