print("Welcome to leap year chec ker")

year=int(input("Enter the year you want to check: "))

if year%4 == 0 and year % 100 != 0 or year %400 == 0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
