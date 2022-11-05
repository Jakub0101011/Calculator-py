# Author: pokczampDev

import os
from datetime import datetime
import time
from colorama import Fore, Back, Style

#Variables
now = datetime.now()
curtime = now.strftime("%H:%M")

# clear all text in cmd
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
# This function percentages two numbers
def percentage(x, y):
    return (x * y) / 100.0

# Main
def kalkulator():
        print(f"""{Fore.RED}
    Calculator by pokczampDev                                           Time: {curtime}
    ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗
    ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
        {Fore.RESET}""")
        print("Select operation.")
        print(f"{Fore.GREEN}| 1 | {Fore.RESET}Add")
        print(f"{Fore.GREEN}| 2 | {Fore.RESET}Subtract")
        print(f"{Fore.GREEN}| 3 | {Fore.RESET}Multiply")
        print(f"{Fore.GREEN}| 4 | {Fore.RESET}Divide")
        print(f"{Fore.GREEN}| 5 | {Fore.RESET}Percent")
        print(f"{Fore.GREEN}| 6 | {Fore.RESET}Exit")

        while True:
            # take input from the user
            choice = input("Enter choice(1/2/3/4/5/6): ")

            # check if choice is one of the four options
            if choice in ('1', '2', '3', '4', '5', '6'):
                try:
                    if choice == '6':
                        clearcmd()
                        quit()
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except (ValueError, TypeError):
                        print(f"{Fore.RED}| ! | {Fore.RESET}Error occurred (you write letter, enter a number)")
                        time.sleep(1)
                        kalkulator()

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                elif choice == '5':
                    print(num1, "-", num2, "=", percentage(num1, num2), "%")

                # check if user wants another calculation
                # break the while loop if answer is no
                next_calculation = input(f"{Fore.YELLOW}| ? | {Fore.RESET}Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                    break

            else:
                print(f"{Fore.RED}| ! | {Fore.RESET}Invalid Input")


def main():
    try:
        clearcmd()
        kalkulator()
    except KeyboardInterrupt:
        print(f"\n{curtime} CTRL + C detected, Going back to the main menu!")
        time.sleep(1)
        kalkulator()
main()