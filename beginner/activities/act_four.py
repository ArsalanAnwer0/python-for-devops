# Dictionary Practice
import random

dict = {"France":"Paris","Japan":"Tokyo","Germany":"Berlin"}

# trying to print dict in formatted way

def printDict():
        print("Countries and Capitals\n")
        for x,y in dict.items():
            print(f"{x}-->{y}")
def check(user_country,user_capital):
        for x,y in dict.items():
        # user_country user_capital == x y 
            if user_country.lower() == x.lower() and user_capital.lower() == y.lower():
             print("Correct! Well done!")

def main(): 
    printDict()
    user_country = random.choice(list(dict.keys())).lower().strip()
    user_capital = input(f"\nGuess the capital of {user_country}: ").strip().lower()
    check(user_country,user_capital)
    choice = input("Add a new country: (yes/no)").strip().lower()
    if choice == "yes":
            country = input("Enter country: ")
            capital = input("Enter capital: ")
            dict[country] = capital
            printDict()
    else:
        print("Program has ended")

  


if __name__ == "__main__":
    main()