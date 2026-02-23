# Take user input
number = int(input("Enter the number: "))
print(f"\nMultiplication Table of {number}:\n")
#take a range from 1 to 10
for i in range(1,11): 
    product = number * i  # calculate multiplication
    #display the result
    print(f"{number} x {i} = {product}")

