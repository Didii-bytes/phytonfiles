numGrades=int(input('How many grades do you have? '))
grades=[]
bucket=0
lowGrade=100
highGrade=0
for i in range (0,numGrades,1):
    grade=float(input('Please Enter your Grade: '))
    grades.append(grade)
print("Your Grades Are:- ")
for i in range(0,numGrades,1):
    print(grades[i])
for i in range(0,numGrades,1):
    bucket=bucket+grades[i]
average=bucket/numGrades
print('')
print('Your Average grade is: ',average)
for i in range(0,numGrades,1):
    if grades[i]<lowGrade:
        lowGrade=grades[i]
print('Your Low Grade is,',lowGrade)
for i in range(1,numGrades,1):
    if grades[i]>highGrade:
        highGrade=grades[i]
print('Your High Grade is, ',highGrade,)
print ('')
print('Congrats!')