print("welcome to love calculator")

name1= input("Enter your name : \n")
name2= input("Enter his/her name : \n")

temp1=name1.lower()
temp2=name2.lower()

full= temp1+temp2

t = full.count("t")
r = full.count("r")
u = full.count("u")
e = full.count("e")

tr= t+r+u+e

l = full.count("l")
o = full.count("o")
v = full.count("v")

love= l+o+v+e

print(f"Your love score is {tr}{love}%")
