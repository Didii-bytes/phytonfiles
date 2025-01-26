numGrade=int(input('How many your grade: '))
grades=[]
bucket=0
lowgrade=100
highgrade=0
for i in range(0,numGrade,1):
    grade=float(input('Whats is your grade: '))
    grades.append(grade)   
for i in range (0,numGrade,1):
    bucket=bucket=+grade
average=bucket/numGrade
print ('Your average grades is,',average,)
for i in range(0,numGrade,1):
    if grades[i]<lowgrade:
        lowgrade=grades[i]
print('Your Lowest grade is,',lowgrade)
for i in range(0,numGrade,1):
    if grades[i]>highgrade:
        highgrade=grades[i]
print('Your Highest grade is,',highgrade)
for i in range(0,numGrade-1,1):
    for i in range(0,numGrade-1,1):
        if grades[i]<grades[i+1]:
            swp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=swp       
print('Your Sorted grade list is, ')
for i in range(0,numGrade,1):
    print(grades[i])
    
