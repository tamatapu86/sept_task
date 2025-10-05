balance = 0

def display_menu():
    print("\n ATM Menu: ")
    print("1. Credit: ")
    print("2. Debit: ")
    print("3. Balance: ")
    print("4. Exit: ")

def choice():
    return input("enter your choice(1-4): ").strip()
def credit():
    global balance
    amount = float(input("Enter the amount to credit: "))
    if amount <= 0:
        print("Invalid amount, please eneter positive amount")
    else:
        balance+=amount
        print(f'{amount} credited to your account')
def debit():
    global balance
    amount = float(input("Enter the amount to with drawl: ").strip())
    if amount <= 0:
        print("Invalid amount, please enter positive amount.")
    elif amount > balance:
        print("Insufficent funds!")
    else:
        balance-=amount
        print(f'{amount} credited to your account')
def show_balance():
    print(f'your current balance is {balance}')

def main():
    while True:
        display_menu()
        select_1 = choice()
        if select_1 == "1":
            credit()
        elif select_1 == "2":
            debit()
        elif select_1== "3":
            show_balance()
        elif select_1 == "4":
            print("Thank you for using ATM, Good bye!")
            break
        else:
            print("Invalid selection, Try again.")
main()




