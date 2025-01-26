import pickle
names=[]
grades=[]
Averages=[]
bucket=0
Student=(input('How many Student in class: '))
for s in range(0,Student,1):
    Name=(input('what is your name: '))
    names.append(Name)
    numGrade=int(input('how many grade do you have?: '))
    bucket=0
    for j in range(0,numGrade,1):
        n1=int(input('Please enter your grade: '))
        grades.append(n1)
    for i in range(0,numGrade,1):
        bucket=bucket+grades[i]
    Average=bucket/numGrade
    Averages.append(Average)
    print(Name,'average grade is,',Average)
with open('ClassGrade','wb') as dataf:
    pickle.dump(Student,dataf)
    pickle.dump(names,dataf)
    pickle.dump(Averages,dataf)
with open ('ClassGrade','rb') as readf2:
    a=pickle.load(readf2)
    b=pickle.load(readf2)
    c=pickle.load(readf2)

print (a)
print (b)
print (c)
