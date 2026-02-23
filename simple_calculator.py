#Simple Calculator
print("---------SIMPLE CALCULATOR---------")
num1=int(input("Enter the First number:"))
num2=int(input("Enter the second number:"))
print("\n results:")
print("Addition: ",num1+num2)
print("Subtraction: ",num1-num2)
print("Multiplication: ",num1*num2)
if(num2 !=0):
  print("Division: ",num1/num2)
  print("Modulus: ",num1%num2)
else:
  print("Cannot divide by zero!")
print("Exponentiation: ",num1**num2)


