def grade_check(scores,grades):
    
    for key in scores:
        score = scores[key]
        if score > 90 and score <= 100:
            grades[key]= "Outstanding"
        elif score > 80 and score<=90:
            grades[key]= "Exceeds Expectations"
        elif score > 70 and score <= 80:
            grades[key]= "Acceptable"
        else:
            grades[key]= "Fail"
    return grades

def print_grades(grades):
    for keys in grades:
        print(f"{keys} -> {grades[keys]}")    

#driver code
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
grade_check(student_scores,student_grades)
print_grades(student_grades)
