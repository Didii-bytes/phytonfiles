def inputGrades(nm): #first function (variable is inputGrades)
    grades=[]
    for i in range(0,nm,1):
        grd=float(input('please enter your grade: '))
        grades.append(grd)
    return grades #result is grades return to myGrades

def printGrades(nm,x): #Second function (variable is printGrades)
    for i in range(0,nm,1):
        print(x[i])
#not return because is only print

def averageGrades(nm,x): #third function(variable is averageGrades)
    tot=0
    for i in  range(0,nm,1):
        tot=tot+x[i]
    average=tot/nm
    return average # result is average return to avg

def highLow(nm,x): #forth function(variable is highLow)
    highG=0
    LowG=100  # set both limit for high and low
    for i in range(0,nm,1):
        if  (x[i]<LowG):
            LowG=x[i]
        if (x[i]>highG):
            highG=x[i]
    return highG,LowG # result is both highG or LowG return as highG or lowG

numGrades=int(input('How many grade do you have? '))
myGrades=inputGrades(numGrades) #first funct variable
#input used in 1,2,3,4 function
print('')
print('Your Grades Are: ')
printGrades(numGrades,myGrades) #sec funct variable
print('')
avg=averageGrades(numGrades,myGrades) #third funct variable
print('Your average is,',round(avg,1))
highG, lowG=highLow(numGrades,myGrades) #forth funct varialbe
print('Your High Grades is:',highG)
print('Your low Grades is:',lowG)
