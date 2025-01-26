import pickle
with open('ClassGrade','rb') as DataF:
    Students=pickle.load(DataF)
    names=pickle.load(DataF)
    Averages=pickle.load(DataF)
while(1==1):
    name=input('which Student Do you want to Check? ')
    for i in range(0,Students,1):
        if(names[i]==name):
            print(name,"'s average grades is ",Averages[i],'.')
        else:
            print("data not available")
                            
