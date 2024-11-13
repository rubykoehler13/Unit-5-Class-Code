"""
Name: Ruby Koehler
Date: 11/6/24
Topic: Functions
"""

def sunny_message():
    print("On a sunny day, sandals are appropriate footwear.")
def rainy_message():
    print("On a rainy day, galoshes are appropriate footwear.")
def snowy_message():
    print("On a snowy day, boots are appropriate footwear.")

def main():
    weather = input("Enter the weather (sunny/rainy/snowy): ")
    if weather == 'sunny':
        sunny_message()
    elif weather == 'rainy':
        rainy_message()
    elif weather == 'snowy':
        snowy_message()
    else:
        print("You chose something invalid, please input one of the correct options.")

if __name__ == "__main__":
    main()
