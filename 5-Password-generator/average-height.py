student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(f"The list of height of the students: {student_heights}")

#sum_height=sum(student_heights)
#list_len= len(student_heights)
sum_height=0
list_len=0

for n in range(0, len(student_heights)):
    sum_height += student_heights[n]
    list_len+=1

avg= sum_height/list_len
avg_round= round(avg)

print(f"The average height of the students are : {avg_round}")