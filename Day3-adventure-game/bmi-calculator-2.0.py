print("Welcome to BMI calculator")

height= float(input("Enter you height in meters: "))
weight= float(input("Enter you weight in Kg: "))

temp= weight/(height ** 2)
bmi= round(temp,1)

print(f"Your BMI value is {bmi}")

if bmi<18.5:
    print("You are underweight")
elif bmi<25:
    print("You have a normal weight")
elif bmi<30:
    print("You are overweight")
elif bmi<35:
    print("You are obese")
else:
    print("You are clinically obese")


