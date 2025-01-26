def tally(x,y):
    #in Function
    z=x+y 
    return z    
#not in Function
a=float(input('Please input your first Number: '))
b=float(input('please input your second Number: '))
c=tally(a,b)
print(c)

#another funtion example
def tally(numnum,myArray):
    tot=0
    for i in range(0,numnum,1):
        tot=tot+myArray[i]
    return tot
nums=5
x=[2,4,6,8,10]
mysum=tally(nums,x)
print('Array Total= ',mysum)

#basic math function
def tally(x,y):
    tot=x+y
    dif=x-y
    prod=x*y
    div=x/y     
    return tot,dif,prod,div # all result should be return 

a=float(input('Please input your first Number: '))
b=float(input('please input your second Number: '))
w,x,y,z=tally(a,b)
print('sum is = ',w)
print('dif is = ',x)
print('prod is = ',y)
print('div is = ',z)

# masukan input dari luar "def" ke dalam "def"
def tally(nums):
    x=[]
    for i in range(0,nums,1):
        myNum=int(input('Enter Your Number'))
        x.append(myNum)
    return x

numNum=int(input('Enter How many number you want: '))
y=tally(numNum)
print(y)