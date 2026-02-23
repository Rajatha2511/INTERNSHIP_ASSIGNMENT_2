#temperature_converter- menu-based system
while True:
    print("\n Temperature Converter Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Celsius to Kelvin")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    choice =  int(input("Enter your choice (1-7):"))
    if choice==1:
        c=float(input("Enter Temperature in celsius:"))
        f=(c*9/5)+32
        print(f"{c}degree Celsius is equal to {f} degree Fahrenheit")
    elif choice==2:
        f=float(input("Enter temperature in Fahrenheit:"))
        c=(f-32)*5/9
        print(f"{f} degree Fahrenheit is equal to {c} degree Celsius")
        


