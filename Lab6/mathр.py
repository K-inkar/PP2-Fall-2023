 # 1.Write a Python program to convert degree to radian.
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print(f"Output radian: {radian:.6f}")

# 2.Write a Python program to calculate the area of a trapezoid.
import math
height = float(input("Height: "))
first_value = float(input("Base, first value: "))
second_value = float(input("Base, second value: "))
area = 0.5 * (first_value + second_value) * height
print(f"Expected Output: {area}")

# 3.Write a Python program to calculate the area of regular polygon.
import math
n = float(input("Number of sides: "))
s = float(input("Length of a side: "))
area = (1/4) * n * s**2 / math.tan(math.pi / n)
round_area = round(area)
print("The area of the polygon is:", round_area)

# 4.Write a Python program to calculate the area of a parallelogram.
import math 
l = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
area = l * h
print("The area of the parallelogram is:", area)
