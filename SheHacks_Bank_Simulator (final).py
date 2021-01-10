# SheHack - Banking Simulator
# Team: Fiorella Russi, Nadia Nguyen, Yasmine Kollar
from random import randint, choice


class Colours:
    pink = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    peach = '\033[91m'
    ENDC = '\033[0m'  # reset
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    highlight = '\033[100m'


life_actions = {"It's time to pay rent! You lose $100.": -100,
                "It's time to pay your phone bill! You lose $20.": -20,
                "You babysit your neighbours kids! You got paid $20.": 20,
                "Your mom forgot to make you lunch, she gave you $10.": 10,
                "You won a Hackathon! Your price was $50, good job hacker!": 50,
                "You slipped on ice on your way home, a stranger gave you $5 for making them laugh.": 5,
                "You scratched your friend's car, you gave them $30 for damages. :(": -30,
                "You got a $20 speeding ticket because you were rushing home to attend a SheHacks workshop.": -20}


class Account:
    def __init__(self):
        self.name = input("What is your name? ")
        self.chequing = ''  # TODO maybe delete, useless unless we do savings acc
        self.savings_balance = 0
        self.bank = ""
        bank_choice = input(f"""Which bank would you like to join today? {Colours.yellow}(a/b/c/d){Colours.ENDC}
a: {Colours.yellow}CIBC{Colours.ENDC}       |
b: {Colours.peach}Scotiabank{Colours.ENDC} |
c: {Colours.green}TD{Colours.ENDC}         |
d: {Colours.blue}BMO{Colours.ENDC}        | Enter choice: """)

        self.balance = 0
        valid_bank_choice = False

        while valid_bank_choice is False:
            valid_bank_choice = True
            if bank_choice == "a":
                self.bank = f"{Colours.yellow}CIBC{Colours.ENDC}"
            elif bank_choice == "b":
                self.bank = f"{Colours.peach}Scotiabank{Colours.ENDC}"
                print("You get a bonus $100 for choosing Scotiabank!")
                self.balance += 100
            elif bank_choice == "c":
                self.bank = f"{Colours.green}TD{Colours.ENDC}"
                print("You get a bonus $100 for choosing TD!")
                self.balance += 100
            elif bank_choice == "d":
                self.bank = f"{Colours.blue}BMO{Colours.ENDC}"
            else:
                valid_bank_choice = False
                bank_choice = input("Invalid choice. Try again: ")

        print(f"\nYour bank is {self.bank}.")
        pin = input("Please set up your pin, must be 4 digits: ")
        pin_accepted = False
        while pin_accepted is False:
            if len(pin) != 4:
                pin = input("Invalid pin. Please try again, your pin must be 4 digits long: ")
            else:
                try:
                    pin = int(pin)

                except ValueError:
                    pin = input("Invalid pin. Please try again, your pin can only contain numerical characters: ")

                else:
                    pin_accepted = True
                    print(f"\n{Colours.highlight}Thank you for joining {self.bank}{Colours.highlight}! Your account is now set up.{Colours.ENDC}")
                    print(f"Your current account balance is: {Colours.green}${str(self.balance)}{Colours.ENDC}")

    def contest(self):
        print(f"\n{self.bank} is having a contest. You can win up to $100!!! Would you like to enter? {Colours.yellow}(Y/N){Colours.ENDC}")
        answer = input().lower()

        if answer == "y":
            number_chosen = randint(1, 10)
            guess = int(input("Guess a number from 1-10: "))

            if guess == number_chosen:
                print("You guessed it!!! You win $100!!! :)")
                self.balance += 100

            elif guess > number_chosen:
                print(f"""Your guess was {guess} and the number chosen was {number_chosen}.
You went over the number, you win $0 :( Better luck next time\n-------""")

            elif guess < number_chosen:
                price = randint(0, 40)
                print(f"""Your guess was {guess} and the number chosen was {number_chosen}.
You win ${price}!!!\n-------""")
                self.balance += price
        else:
            print(f"{Colours.pink}Woww really? You could've won some easy cash but ok.{Colours.ENDC}\n----------")

    def actions(self):
        print(f"\nHello {self.name}!")
        print(f"{Colours.highlight}Your current Chequings account balance is ${self.balance}{Colours.ENDC}")
        print(f"{Colours.highlight}Your current Savings account balance is ${self.savings_balance}{Colours.ENDC}")
        print(f"{Colours.UNDERLINE}What would you like to do today?{Colours.ENDC}")
        print(f"""{Colours.yellow}1:{Colours.ENDC} Deposit money into Chequings
{Colours.yellow}2:{Colours.ENDC} Withdraw money from Chequings
{Colours.yellow}3:{Colours.ENDC} Life event (Randomly win or lose money based on daily life events)\t
{Colours.yellow}4:{Colours.ENDC} Enter {self.bank} contest
{Colours.yellow}5:{Colours.ENDC} Transfer money from Chequings into Savings
{Colours.yellow}6:{Colours.ENDC} View Savings account balance over time
{Colours.yellow}7:{Colours.ENDC} Exit""")
        action_choice = int(input("Enter choice: "))

        if action_choice == 1:
            deposit_amount = int(input("Enter the amount you would like to deposit: $"))
            self.balance += deposit_amount

        elif action_choice == 2:
            withdraw_amount = int(input("Enter the amount you would like to withdraw: $"))
            self.balance -= withdraw_amount

        elif action_choice == 3:
            event = None
            global life_actions
            event = choice(list(life_actions.keys()))
            money = life_actions.get(event)
            print(f"{Colours.cyan}{event}{Colours.ENDC}")
            self.balance += money

        elif action_choice == 4:
            self.contest()
        
        elif action_choice == 5:
            print(f"{Colours.highlight}Your current Chequings account balance is ${self.balance}{Colours.ENDC}")
            if self.balance <= 0:
                print("There are no funds in Chequings account to transfer.")
            else:
                valid_transfer_amount = False
                while valid_transfer_amount is False:
                    transfer_amount = int(input("Enter the amount you would like to transfer from Chequings into Savings: $"))
                    if transfer_amount <= self.balance and self.balance >= 0:
                        self.savings_balance += transfer_amount
                        self.balance -= transfer_amount
                        valid_transfer_amount = True
                    else:
                        print("Invalid transfer amount, must be equal to or less than the Chequings balance.")

        elif action_choice == 6:
            print(f"{Colours.highlight}Your current Savings account balance is ${self.savings_balance}{Colours.ENDC}")
            print("With a 0.08% yearly interest rate (Simple Interest Calculated):")
            balance_1_year = self.savings_balance*1.0008
            balance_5_year = self.savings_balance*(1+0.0008*5)
            balance_10_year = self.savings_balance*(1+0.0008*10)

            print(f"\tIn 1 year, your Savings account balance will be {Colours.green}${balance_1_year:.2f}{Colours.ENDC}")
            print(f"\tIn 5 years, your Savings account balance will be {Colours.green}${balance_5_year:.2f}{Colours.ENDC}")
            print(f"\tIn 10 years, your Savings account balance will be {Colours.green}${balance_10_year:.2f}{Colours.ENDC}")
        
        elif action_choice == 7:
            global continue_program
            continue_program = False
            return continue_program

        print(f"Your current Chequings account balance is:{Colours.green} ${str(self.balance)}{Colours.ENDC}")
        print(f"Your current Savings account balance is:{Colours.green} ${str(self.savings_balance)}{Colours.ENDC}")
        continue_program = True
        return continue_program


def main():
    account = Account()
    continue_program = True
    user_choice = "y"
    account.contest()
    while continue_program is True and user_choice == 'y':
        continue_program = account.actions()
        if continue_program is True:
            user_choice = input(f"Would you like to continue? {Colours.yellow}(Y/N){Colours.ENDC}").lower()
    
    print(f"\nThank you for using {account.bank}! Goodbye =)")

    input()  # extra input at the end so it doesn't close at the end when opened with Python


main()
