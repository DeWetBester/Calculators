# Alle produkte wat koopbaar is, geplaas in n lys 
products = [('melk', 28.00),
            ('kaas', 120.00),
            ('brood', 25.00),
            ('water', 10.00),
            ('waatlemoen', 15.00),
            ('skottelgoedseep', 78.00),
            ('hoender', 72.00),
            ('mince', 45.00),
            ('tjips', 23.00),
            ('sjokolade', 30.00)
]

# Funksie wat alle produkte wys met hul pryse in Rand en sent
def displayproducts():
    print('\n--- Available Products ---')
    for product, price in products:
        print(f'{product.capitalize()} - R{price:.2f}')
    print('----------------------------')

# Funksie wat die gebruiker se keuses en hoeveelheid van n produk/produkte wat gekies is
def processorder():
    order = []
    totalprice = 0 

    print('\nTo add items to your order, type the product name exactly as shown above.')
    print('When you are finished, type "done" to see your order summary.')

    # Sentinel om die loop te beheer
    sentinel = False

    while not sentinel:
        
        # Ask user to enter a product or "done" to finish
        userinput = input('Enter a product name or "done" to finish: ').lower()

        if userinput == 'done':
            sentinel = True
            continue  # This ensures the user can type "done" to exit

        # Kyk of die produk gevind was in die lys van produkte
        productfound = False

        # Loop deur die lys om te kyk of die produk beskikbaar is
        for product, price in products:
            if userinput == product:
                while True:
                    try:
                        quantity = int(input(f'How many {product}s would you like to buy? '))
                        if quantity > 0:
                            break  # Valid input, break out of the loop
                        else:
                            print('Please enter a valid quantity.')
                    except ValueError:
                        print('Invalid input. Please enter a valid quantity.')

                # Sit die produkte met hul pryse by die bestelling
                order.append((product, price, quantity))  # Add to order list
                totalprice += price * quantity  # Update total price
                print(f'{quantity} x {product.capitalize()} added to your order!')
                productfound = True
                break  # Break after finding the product

        # Laat weet die gebruiker as die produk nie gevind was nie
        if not productfound:
            print('Product not found. Please try again.')

    # Show the order summary correctly
    print('\n--- Your Order Summary ---')
    for product, price, quantity in order:
        print(f'{product.capitalize()} x {quantity} - R{price * quantity:.2f}')  # Price for each item

    # Show the total price correctly after all items are added
    print(f'\nTotal: R{totalprice:.2f}')
    return totalprice

# Funksie wat die POS system run
def possystem():
    print('Welcome to my POS system!')

    while True:
        displayproducts()  # Show products

        total = processorder()  # Process the order and calculate total

        # Vra gebruiker of hulle nog n bestelling wil maak
        repeat = input('\nWould you like to make another purchase? (yes/no): ').lower()
        if repeat != 'yes':
            print('Thank you for shopping with me! Have a great day!')
            break  # Exit if user does not want to buy more

if __name__ == '__main__':
    possystem()