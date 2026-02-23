# Leap Year Checker
year = int(input("Enter a year: "))
if year % 400 == 0:
    print(f"{year} is a Leap Year. Reason: Divisible by 400.")
elif year % 100 == 0:
    print(f"{year} is NOT a Leap Year. Reason: Divisible by 100 but not by 400.")
elif year % 4 == 0:
    print(f"{year} is a Leap Year. Reason: Divisible by 4 but not by 100.")
else:
    print(f"{year} is NOT a Leap Year. Reason: Not divisible by 4.")

