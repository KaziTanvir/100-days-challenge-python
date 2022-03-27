from sympy import false, true


def isprime(number):
    check= true
    for i in range(2,number):
        if number % i==0:
            check=false
    if check:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
n=int(input("Enter your number: "))
isprime(n)