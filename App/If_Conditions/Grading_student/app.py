"""
Write a program to assign grade for student's exams:
A= 90 – 100 (90% - 100%)
B= 80 – 89 (80% - 89%)
C = 70 – 79 (70% - 79%)
F < 69 (Below 69%)

Algorithm
- Get student
- Get test score
- Check test score if it's within range
- Assign Grade
"""
studentName = input("Enter Student Name: ")
studentScore = float(input("Enter Student Score: "))

if(studentScore >= 90 and studentScore <= 100):
    print(studentName, " got A")
elif(studentScore >= 80 and studentScore <= 89):
    print(studentName, " got B")