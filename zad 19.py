import math
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

p = (a+b+c)/2

area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Area: {area}")