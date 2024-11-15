import math
"""
Name: Mr. Smith
Date: 11/13/24
Topic: Returns
"""

# A special calculator

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2): # what about division by 0
    return num1/num2

def num_squared(num1):
    return num1*num1

def pythagorean_solver(a,b):
    c = math.sqrt(num_squared(a)+num_squared(b)) # only works with returns
    return c

def main():
    while True:
        print("What operation do you want to perform: ")
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Right Triangle Solver\n-1.Exit")
        user_choice = int(input("> "))
        if user_choice == 1:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            user_sum = add(num1,num2)
            print(f"{num1} + {num2} = {user_sum}")
        elif user_choice == 2:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            user_diff = subtract(num1, num2)
            print(f"{num1} + {num2} = {user_diff}")
        elif user_choice == 3:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            user_product = multiply(num1, num2)
            print(f"{num1} + {num2} = {user_product}")
        elif user_choice == 5:
            a = int(input("Enter leg a: "))
            b = int(input("Enter leg b: "))
            c = pythagorean_solver(a,b)
            print(f"The hypotenuse c is {c:.2f}")
        elif user_choice == -1:
            break

if __name__ == '__main__':
    main()