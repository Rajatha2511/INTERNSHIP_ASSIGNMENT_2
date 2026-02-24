# Restaurant Bill Splitter
# take inputs from the user 
total_bill = float(input("Enter the total bill amount: ₹"))
people_count = int(input("Enter the number of people: "))
tax_percent = float(input("Enter tax percentage (%): "))
tip_percent = float(input("Enter tip percentage (%): "))
# Calculate the bill
tax_amount = (tax_percent / 100) * total_bill
bill_after_tax = total_bill + tax_amount
tip_amount = (tip_percent / 100) * bill_after_tax
total_amount = bill_after_tax + tip_amount
amount_per_person = total_amount / people_count

# Display
print("\n----- Bill Summary -----")
print(f"Subtotal: ₹{total_bill:.2f}")
print(f"Tax Amount: ₹{tax_amount:.2f}")
print(f"Bill After Tax: ₹{bill_after_tax:.2f}")
print(f"Tip Amount: ₹{tip_amount:.2f}")
print(f"Total Bill: ₹{total_amount:.2f}")
print(f"Amount Per Person ({people_count} people): ₹{amount_per_person:.2f}")

