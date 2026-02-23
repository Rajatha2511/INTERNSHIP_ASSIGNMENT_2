#Student marks and grade calculator
#take user inputs for marks in 5 subjects
math=float(input("enter marks obtained in mathematics:"))
science=float(input("enter marks obtained in science:"))
english=float(input("enter marks obtained in english:"))
history=float(input("enter marks obtained in history:"))
kannada=float(input("enter marks obtained in kannada:"))
#display the marks
print("marks obtained in each subject:")
print(f"Mathematics: {math}")
print(f"Science: {science}")
print(f"English: {english}")
print(f"History: {history}")
print(f"Kannada: {kannada}")
#calculate total marks and percentage
total_marks=math+science+english+history+kannada
percentage=(total_marks/500)*100
#display total marks and percentage
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage}:.2f")
#grade calculation
if percentage>=90:
    Grade="A+(Outstanding)"
elif percentage>=80:
    Grade="A(Excellent)"
elif percentage>=70:
    Grade="B(Good)"
elif percentage>=60:
    Grade="C(Average)"
elif percentage>=50:
    Grade="D(Pass)"
else:
    Grade="F(Fail)"
#display the grade
print(f"Grade: {Grade}")

