# module = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program reusable separate files

# print(help("modules"))
# math module:
import math
import exampl_module

result = exampl_module.pi
print(result)  # OUT -> 3.14159
result = exampl_module.square(3)
print(result)  # OUT -> 9
result = exampl_module.cube(3)
print(result)  # OUT -> 27
result = exampl_module.circumference(3)
print(result)  # OUT -> 18.849539999999998
result = exampl_module.area(3)
print(result)  # OUT -> 28.27431
