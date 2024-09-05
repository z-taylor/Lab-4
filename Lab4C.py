balance = 1000
print(f"Welcome!\nYou have ${balance} in your account.\n")
run = True
while run:
    print("Menu\n0 – Make a deposit\n1 – Make a withdrawal\n2 – Display account value\n")
    opt = int(input("Please make a selection: "))
    match (opt):
        case opt if opt == 0:
            balance = balance + (float(input("How much would you like to deposit?: ")))
            print(f"Your current balance is ${balance}")
        case opt if opt == 1:
            withdrawal = float(input("How much would you like to withdraw?: "))
            if balance >= withdrawal:
                balance = (balance - withdrawal) 
            else:
                print("Not enough balance. Withdrawal cancelled.")
            print(f"Your current balance is ${balance}")
        case opt if opt == 2:
            print(f"Your current balance is ${balance}")
        case _:
            print("Invalid entry, please try again.")
    run = True if input("Would you like to return to the main menu (Y/N)?: ").lower() == "y" else False
print("Thank you for banking with us!")