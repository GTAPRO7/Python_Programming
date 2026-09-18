##Math

import math

print(math.sqrt(25))
print(math.pow(2,3))
print(math.pi)

print("\nImport only sqrt and fact.............")
from math import sqrt, factorial

print(sqrt(36))
print(factorial(5))

print("\nImport math as m.............")
import math as m

print(m.sqrt(49))
print(m.pi)

print("\nImport Statistics.............")
import statistics

marks = [79, 85, 92, 67, 88]

avg = statistics.mean(marks)
md = statistics.median(marks)
std_dev = statistics.stdev(marks)

print("Marks :",marks)
print("Average :",avg)
print("Median :", md)
print("Standard Deviatiom :",std_dev)
