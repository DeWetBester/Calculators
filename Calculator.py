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
import os
import math

def clear_screen():
    # Maak die skerm skoon
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')  

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Maak seker dat niks deur nul gedeel kan word nie en n error wys vir gebruiker as dit gebeur
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    # Kode wat program gaan laat werk
    while True:
        print("Simple Command Line Calculator")
        print("Select operations (separate multiple choices with commas):")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation (x^y)")
        print("6. Square Root (√x)")
        print("7. Sine (sin x)")
        print("8. Cosine (cos x)")
        print("9. Tangent (tan x)")
        print("10. Clear Screen")
        print("11. Exit")

        # Kry die gebruiker se keuse van watse verwerking hy/sy wil doen (meerdere keuses moontlik)
        choices = input("Enter choices (e.g., 1,2,3 for Add, Subtract, Multiply): ")

        # As die gebruiker "11" kies, sal die program stop
        if '11' in choices:
            print("Exiting calculator. Goodbye!")
            break
        
        if '10' in choices:
            clear_screen()  # Maak die skerm skoon
            print("Screen cleared!")
            input("Press Enter to continue...")  
            continue  

        # Verkry die getalle van die gebruiker
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter a valid numeric value.")
            input("Press Enter to continue...")  
            continue 

        # Loop deur die keuses van die gebruiker en verrig die toep geselskap
        for choice in choices.split(','):
            choice = choice.strip()  
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
                if isinstance(result, str):
                    print(result)  # Foutboodskap vir deling deur nul
                else:
                    print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                result = exponentiate(num1, num2)
                print(f"{num1} ^ {num2} = {result}")
            elif choice == '6':
                result = square_root(num1)
                print(f"√{num1} = {result}")
            elif choice == '7':
                result = sine(num1)
                print(f"sin({num1}) = {result}")
            elif choice == '8':
                result = cosine(num1)
                print(f"cos({num1}) = {result}")
            elif choice == '9':
                result = tangent(num1)
                print(f"tan({num1}) = {result}")
            else:
                print(f"Invalid choice {choice}! Please choose a valid operation.")

       
        input("\nPress Enter to continue...")

# Roep die calculator funksie aan
calculator()
