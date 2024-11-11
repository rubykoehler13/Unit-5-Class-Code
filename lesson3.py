'''
Name: Ruby Koehler
Date: 11/8/24
Topic: More parameters
'''

def name_printer(a="John", b="Doe"):
    print(f"Hello, {a} {b}!")


name_printer("Norman", "Roberts")
name_printer("Bob")
name_printer()

########################################################################################

'''
Write a function that takes in two parameters, a person's name and their favorite color.
Print out their name in the form "<name> the fierce, <color> eyed warrior"

If they choose not to enter a favorite color, make the default color yellow.
'''

def statement(name, fav_color="yellow"):
    print(f"{name} the fierce, {fav_color} eyed warrior.")

statement("Ruby", "red")
statement("Sam")

########################################################################################

'''
Write a function called blackjack that takes in three integer parameters.
The numbers should be between 1 and 11. 
If their sum is less than or equal to 21, print the sum. 
If the sum exceeds 21 and there is an 11, print the sum reduced by 10. 
If the sum exceeds 21, print BUST. 
If an integer outside of 1-11 is entered, print ERROR.
'''

def blackjack(num_1, num_2, num_3):
    sum = (num_1 + num_2 + num_3)
    valid_numbers = 1 <= num_1 <= 11 and 1 <= num_2 <= 11 and 1 <= num_3 <= 11
    if not valid_numbers:
        print("ERROR")
    elif sum <= 21:
        print(sum)
    elif sum > 21 and (num_1 == 11 or num_2 == 11 or num_3 == 11):
        print(sum-10)
    elif sum > 21:
        print ("BUST")

blackjack(2, 5, 11)
blackjack(10, 5, 6)
blackjack(10, 10, 11)
blackjack(21, 31, 12)

########################################################################################