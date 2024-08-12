#BMI = weight inkgs/(height in m)^2

weight =float(input("Enter weight in kgs"))
height =float(input("Enter height in meters"))
bmi = weight/(height**2)
print(f"BMI is {bmi}")
