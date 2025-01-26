numGrade=int(input('how many your grade: '))
j=0
grade=[]
while(j<numGrade):
    n1=input('what is your grade?: ')
    grade.append(n1)
    j=j+1
print('ini markah anda: ')
for i in range(0,numGrade,1):
    print(grade[i])
print('')
print('itu je Thanks!')
