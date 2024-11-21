def calculate_total_cost(a, b=15):
    return ((a*b)/100)+a

def main():
    while True:
        try:
            meal_cost = float(input("Enter the meal cost: "))
            tip_percentage = int(input("Enter the tip percentage: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for meal cost and tip percentage.")
            continue
        cost = round(calculate_total_cost(meal_cost, tip_percentage), 2)
        print(f"The total cost of the meal is: ${cost}")
        break
# I am so confused on how I would call the function that has default parameters when
# the user inputs a negative number, because the function is global but the variables
# are local. I tried doing "global" before my variables so that I could call them from
# outside the main() function, but that didn't work! I also tried doing everything inside
# the main() function which also didn't work. I'm just super confused
if __name__ == '__main__':
    main()