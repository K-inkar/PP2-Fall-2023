#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input("Grams: "))
ounces = grams_to_ounces(grams)
print(f"{ounces} ounces")

#2
def f_to_c():
    f = float(input("Fahrenheit: "))
    c = (5 / 9) * (f - 32)
    return c

c_temperature = f_to_c()
print(f"Celsius: {c_temperature:.2f} °C")

#3
def solve(numheads, numlegs):
    for chic in range(numheads + 1):
        rab = numheads - chic
        if (2 * chic + 4 * rab) == numlegs:
            return chic, rab
    return None

numheads = int.input()  #numheads = 35
numlegs = int.input() #numlegs = 94 
answ = solve(numheads, numlegs)

if answ:
    c, r = answ
    print(f"Chickens: {c}")
    print(f"Rabbits: {r}")
else:
    print("No solution")

#4
def filter_prime(a):
    b = []
    for i in range(len(a)):
        if a[i] == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                b.append(i)
    return b         
a = [int(s) for s in input().split()]
result = filter_prime(a)
print(result, end = ' ')

#5
def get_permutations(s, prefix=""):
    n = len(s)
    if n == 0:
        print(prefix)
    else:
        for i in range(n):
            get_permutations(s[:i] + s[i+1:], prefix + s[i])

user_input = input()
print()
get_permutations(user_input)

#6
def rev(s):
    w = s.split()
    rev_s = " ".join(reversed(w))
    return rev_s

x = input()
rev_s = rev(x)
print(rev_s)

#7
def has_33(N):
    for i in range(len(N) - 1):
        if N[i] == 3 and N[i + 1] == 3:
            return True
    return False

N = [int(s) for s in input().split()]
print(has_33(N))

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

nums = [int(s) for s in input().split()]
print(sky_game(nums))

#9
def v(r):
    v = 4*(r*r*r*3.14)/3
    print(v) 
r = int(input())
v(r)

#10
def unique(input_list):
    lst = []
    for item in input_list:
        if item not in lst:
            lst.append(item)
    return lst

user_input = input()
numbers = [int(x) for x in user_input.split()]
result = unique(numbers)
print(result)

#11
def palindrome_word(word):
    w = word[::-1]
    if(word == w):
        print('Its a palindrome')
    else:
        print('Its not a palindrome')

word = str(input())
palindrome_word(word)

#12
def histogram():
    input_str = input()
    numbers = [int(num) for num in input_str.split()]
    
    for num in numbers:
        print('*' * num)
histogram()

#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number_to_guess = random.randint(1, 20)
    guesses = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
