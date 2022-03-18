print("Welcome to tip calculator")
bill= float(input("What is your total bill? "))
tip_p= float(input("What percentage tip you want to pay? "))
people= int(input("How many people will split the bill? "))

billAndTip= bill + (bill*(tip_p/100))

f_bill= billAndTip/people
final_amount=round(f_bill,2)

print(f"Each person should pay: {final_amount}")