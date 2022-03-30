def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    x=float(a)/float(b)
    res= round(x,3)    
    return res

from art import logo
print(logo)

print("Welcome to Simple Claculator \n You can use +,-,*,/ \n Enter the expression in First number (operator) second number")
end_check= False

operators = ["+","-","*","/"] 

c=0
while not end_check:    
    n1=0
    n2=0
    n3=""
    n4=""
    op=""
    c=0
    exp = input("Please input your aruthmatic expression: \n")
    for i in range(0,len(exp)):
        if exp[i] in operators:
            op= exp[i]
            break
        c +=1
    
    for i in range(0,c):
        n3 += exp[i]
    for i in range(c+1,len(exp)):
        n4 += exp[i] 
    n1=int(n3)
    n2= int(n4)
    
    operations = {
        "+" : add(n1,n2),
        "-" : substract(n1,n2),
        "*" : multiply(n1,n2),
        "/" : divide(n1,n2)
    }
    res = operations[op]
    print(f"Your result is = {res}")
    
    check= input("Do you want to do another calculation? Y or N \n").lower()
    if check== "n":
        end_check = True


