# temperature_converter - Menu Based System
while True:
    print("\nTemperature Converter Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Celsius to Kelvin")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    
    # Take user input for menu choice
    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:  # Celsius to Fahrenheit
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c} degree Celsius is equal to {f} degree Fahrenheit")

    elif choice == 2:  # Fahrenheit to Celsius
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f} degree Fahrenheit is equal to {c} degree Celsius")

    elif choice == 3:  # Kelvin to Celsius
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273.15
        print(f"{k} degree Kelvin is equal to {c} degree Celsius")

    elif choice == 4:  # Celsius to Kelvin
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print(f"{c} degree Celsius is equal to {k} degree Kelvin")

    elif choice == 5:  # Fahrenheit to Kelvin
        f = float(input("Enter temperature in Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"{f} degree Fahrenheit is equal to {k} degree Kelvin")

    elif choice == 6:  # Kelvin to Fahrenheit
        k = float(input("Enter temperature in Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"{k} degree Kelvin is equal to {f} degree Fahrenheit")

    elif choice == 7:  # Exit
        print("Exiting the program. Goodbye!")
        break

    else:  # Invalid input
        print("Invalid choice! Please enter a number between 1 and 7.")
    
