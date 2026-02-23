# Sum and Average Calculator
print("------ SUM AND AVERAGE CALCULATOR ------")
# Ask user how many numbers they want to enter
count = int(input("Enter the number of numbers you want to enter? "))
# Initialize total, maximum, and minimum 
total = 0
maximum = None
minimum = None
for i in range(1, count + 1):
    num = int(input("Enter number " + str(i) + ": "))
    total=total+num  # Add to total

    # Set maximum and minimum for the first number
    if i == 1:
        maximum = num
        minimum = num
    else:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

# Calculate average (only if count > 0)
if count > 0:
    average = total / count
else:
    average = 0

# Print results
print("\nResults:")
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
