numGrades=int(input('How many grades do you have? '))
grades=[]
bucket=0
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
print('Congrats!')


