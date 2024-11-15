"""
Name: Mr. Smith
Date: 11/6/24
Topic: Functions
"""

def sunny_message():
    print("On a sunny day, sandals are appropriate footwear.")
    pass

def rainy_message():
    print("On a rainy day, galoshes are appropriate footwear.")

def snowy_message():
    print("On a snowy day, boots are appropriate footwear.")

def main():
    # ask the user for the weather
    weather = input("What is the weather? (sunny, rainy, snowy): ")
    # if statements to decide which function
    # to run
    if weather.lower() == "rainy":
        rainy_message()
    elif weather.lower() == "sunny":
        sunny_message()
    elif weather.lower() == "snowy":
        snowy_message()
    else:
        print("Invalid option")

if __name__ == '__main__':
    main()