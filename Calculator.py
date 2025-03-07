import os

def clear_screen():
    """Function to clear the terminal screen."""
    if os.name == 'nt':
        os.system('cls')  
    

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 
    return x / y

def calculator():
    while True:
       
        clear_screen()

        print("Simple Command Line Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input! Please choose a valid operation.")
            continue
        
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter a valid numeric value.")
            continue

       
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        
        input("\nPress Enter to continue...")


calculator()
