# 1.Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

numbers = input()
numbers = [float(num) for num in numbers.split()]
result = reduce(lambda x, y: x * y, numbers)
print(result)

# 2.Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
text = input()
upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("upper case:", upper)
print("lower case:", lower)

# 3.Write a Python program with builtin function that checks whether a passed string is palindrome or not.
text = input()
text = text.replace(" ", "").lower()
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 4.Write a Python program that invoke square root function after specific milliseconds.
import math
import time

number = float(input())
milliseconds = int(input())
seconds = milliseconds / 1000
time.sleep(seconds)
square_root = math.sqrt(number)
print(number)

# 5.Write a Python program with builtin function that returns True if all elements of the tuple are true.
elements = eval(input()) #True, False, True...
result = all(elements)
if result:
    print("All elements in the tuple are True.")
else:
    print("Not all elements in the tuple are True.")


