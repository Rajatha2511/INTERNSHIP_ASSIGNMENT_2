number = int(input("Enter a number:"))
if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("0!=1")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial= factorial*i
    steps=''
    for i in range(number,0,-1):
        steps+=str(i)
        if i!=1:
            steps+='*'
    print(f"{number}!={steps}={factorial}")
    
    
    
    


