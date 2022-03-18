from calendar import month


print("Welcome to life span calculator")

age = int(input("Enter your age in years: "))

years = int(90-age)
days = int(years*365)
weeks = int(days/7)
months = int(years*12)

print(f"Assuming your life span is hopefully 90 years you have {years} years or {months} months or {weeks} weeks or {days} days left")
