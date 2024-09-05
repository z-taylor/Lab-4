print("Welcome!")
num = float(input("Please input a number: "))
opt = int(input("What would you like to do to this number:\n0) Get the additive inverse of the number\n1) Get the reciprocal of the number\n2) Square the number\n3) Cube the number\n4) Exit the program\n"))
match (opt):
    case opt if opt==0:
        print(f"The additive inverse of {num} is {(num*-1)}")
    case opt if opt==1:
        if num == 0.0:
            print("Cannot divide by 0!")
        else:
            print(f"The reciprocal of {num} is {(1/num)}")
    case opt if opt==2:
        print(f"The square of {num} is {(num**2)}")
    case opt if opt==3:
        print(f"The cube of {num} is {(num**3)}")
    case opt if opt==4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid input, please try again!")
