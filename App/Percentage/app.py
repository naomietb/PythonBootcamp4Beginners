import os
# Clearing the Screen
os.system('cls')


# Number of questions
numberOfQuestion = 80
# Marks per question
markPerQuestion = 4
# Calculating total marks for the test
totalMarksForTest = numberOfQuestion * markPerQuestion
# Number of questions the student got correct
numberOfCorrectQuestions = 78
# Calculation total marks for stdent
totalMarksForStudent = numberOfCorrectQuestions * markPerQuestion
# Calculating percentage
percentage = (totalMarksForStudent / totalMarksForTest) * 100