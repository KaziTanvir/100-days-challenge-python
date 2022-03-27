import math

from numpy import mat
def can_required( length, width):
    cans_req = (length*width)/5
    cans_req_final = math.ceil(cans_req)
    return cans_req_final    


length = float(input("Enter the length of the wall: "))
width = float(input("Enter the width of the wall: "))

print(f"The amount cans required are {can_required(length,width)} cans")


