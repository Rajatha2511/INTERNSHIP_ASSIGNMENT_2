#prime number checker
number=int(input("Enter a number to check if it is prime:"))#take user input for number
#check if a number is prime or not
if number<=1:
    print(f"{number} is not a prime number")
elif number==2:
    print(f"{number} is a prime number")
else:
    for i in range(2, number):#check divisibility from 2 to number-1
        if number % i==0:
            print (f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
# find all prime numbers in a given range
start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range:"))
print(f"Prime numbers between {start} and {end} are:")
for number in range(max(2, start), end + 1):#starts from 2 because the prime numbers start from 2
    for i in range(2,number):
        if number%i==0:
            break
    else:
             print(number,end=" ")




    