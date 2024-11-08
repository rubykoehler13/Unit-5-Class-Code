'''
Write a function called name_printer that takes in two string parameters first_name and last_name and prints a greeting.
Here are some sample function calls - notice the default parameters

name_printer("Norman","Roberts")
name_printer("Bob")
name_printer()

Hello, Norman Roberts!
Hello, Bob Doe!
Hello, John Doe!
'''

def name_printer(first_name="Starla",last_name="Doe"):
    print(f"Hello, {first_name} {last_name}!")

'''
Write a function that takes in two parameters, a person's name
and their favorite color. Print out their name in the form
"<name> the fierce, <color> eyed warrior"

If they choose not to enter a favorite color, make the default color
yellow
'''

'''
Write a function called blackjack that takes in three integer parameters. The numbers
should be between 1 and 11. If their sum is less than or equal to 21, print the sum. If
the sum exceeds 21 and there is an 11, print the sum reduced by 10. If the sum exceeds 21,
print BUST. If an integer outside of 1-11 is entered, print ERROR.
'''


def main():
    name_printer("Norman","Brewer")
    name_printer("Wilson")



if __name__ == '__main__':
    main()