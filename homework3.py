
x=int(input('How many Grade did you have: '))
grades=[]
for i in range (0,x,1):
    grade=float(input('Please Enter your Grade: '))
    grades.append(grade)
    print(grades)
print( 'Your Grades Are:')
for i in range (0,x,1):
    print(grades[i])
print('Congratulations!')