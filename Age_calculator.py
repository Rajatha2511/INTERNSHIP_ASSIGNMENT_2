#Age calculator
#take user input for birth year
birth_year= int(input("Enter your birth year:"))
current_year=2025
#calculate age
age_years=current_year-(birth_year)
age_months=age_years*12
age_days=age_years*365
age_hours=age_days*24
age_minutes=age_hours*60
years_remaining=100-age_years
#print the age in years, months, days, hours and minutes
print(f"Your age in years : {age_years}")
print(f"Your age in months : {age_months}")
print(f"Your age in days : {age_days}")
print(f"Your age in hours : {age_hours}")
print(f"Your age in minutes : {age_minutes}")
#print the years remaining to reach 100 years
print(f"years remaining to reach 100 years: {years_remaining} years")

