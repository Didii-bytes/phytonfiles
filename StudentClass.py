class Students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def gInput(self,ng):
        self.ng=ng
        self.grades=[]
        for i in range(0,ng,1):
            prompt=('Please Enter '+self.first+"'s grade: ")
            grd=float(input(prompt))
            self.grades.append(grd)
        return self.grades
    def printGrades(self):
        print(self.first,self.last,"'s Grades are: ")
        for i in range(0,self.ng,1):
            print(self.grades[i])     
    def avGrades(self):
        bucket=0
        for i in range(0,self.ng,1):
            bucket=bucket+self.grades[i]
        avg=bucket/self.ng
        return avg
    def HighLow(self):
        Hg=0
        Lg=100
        for i in range(0,self.ng,1):
            if self.grades[i]<Lg:
                Lg=self.grades[i]
            if self.grades[i]>Hg:
                Hg=self.grades[i]
        return Lg,Hg 

student1=Students('joe','Evans')
student2=Students('Shirly','Baker')
print(student1.first,student1.last)
print(student2.first,student2.last)

student1.gInput(4)
student2.gInput(6)
print('')
student1.printGrades()
avg=student1.avGrades()
print(student1.first,'has an average of',avg)
LowG,highG=student1.HighLow()
print('Low grades is,',LowG)
print('High grade,',highG)
print('')
student2.printGrades()
avg=student2.avGrades()
print(student2.first,'has an average of',avg)
LowG,highG=student2.HighLow()
print('Low grades is,',LowG)
print('High grade,',highG)

#student1.gInput(4) # from self.gInput
#student1.printGrades()
#print(student1.grades) #from self.grades
#avg=student1.avGrades()
#print(student1.first,'has an average of',avg)
#LowG,highG=student1.HighLow()
#print('Low grades is,',LowG)
#print('High grade,',highG)
