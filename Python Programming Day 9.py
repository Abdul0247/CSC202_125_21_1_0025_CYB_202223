# Grading Program

student_scores = {
    "Alice": 81,
    "Bob": 78,
    "Claire": 99,
    "Dan": 74,
    "Evang": 62,
}

student_score = {}

for i in student_scores:
    mark = student_scores[i]
    if mark <= 70:
        student_score[mark] = "Fail"
        
    elif mark >= 71 and mark <= 80:
        student_score[mark] = "Acceptable"
        
    elif mark >= 81 and mark <= 90:
        student_score[mark] = "Exceeds expectation"
    
    elif mark >= 91 and mark <= 100:
        student_score[mark] = "Outstanding"
        
print(student_score)

