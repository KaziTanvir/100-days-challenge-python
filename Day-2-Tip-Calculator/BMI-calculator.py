print("Welcome to BMI calculator")

weight=float(input("Enter your weight in Kg: "))
height=float(input("Enter your height in Meter: "))

bmi= weight/height**2

f_bmi=round(bmi,2)

print(f"Your BMI value is : {f_bmi}")
