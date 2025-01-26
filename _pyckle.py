import pickle
fruit=['apple','orange','banana']
x=7
y=3.14
nuts=['pecans','almond']
grades=[99,100,56,77,85]
dataset=[fruit,x,y,nuts,grades]
with open('myData.pkl','wb') as f:
    pickle.dump(dataset,f)
with open ('myData.pkl','rb') as f2:
    a=pickle.load(f2)
for dt in a:
    print(dt)  
    
