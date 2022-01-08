l=[[1,2,3],[4,5,6],[7,8,9]]
print(l)
for i in l:
       for j in i:
           print(j,end=" ")
print()

# LIST MERGE PROGRAM

def listmerge(l1,l2):
    l3=[]
    for x in l1:
        l3.append(x)
    for x in l2:
        l3.append(x)
    print(l3)
    for x in l3:
        print(x)
l1=[]
l2=[]
n=int(input("Enter the size :")) 
for i in range(1,n+1):
    data=int(input("Enter the data :"))
    l1.append(data)
for i in range(1,n+1):
    data=int(input("enter the data :"))
    l2.append(data)    
print(l1)
print(l2)
listmerge(l1,l2)                   

# LIST SWAPING PROGRAM

def listswap(l):
    temp=0
    for x in range(len(l)):
        temp=l[0]
        l[0]=l[x-1]
        l[x-1]=temp
    print(l)
l=[]
n=int(input("Enter the size :"))
for i in range(1,n+1):
    data=int(input("Enter the data"))
    l.append(data)
print(l)
listswap(l)    

# LAST AND FIRST INDEX DATA SWAP PROGRAM
def listswap(l1):
    temp=0
    size=len(l1)
    print(l1)
    temp=l1[0]
    l1[0]=l1[size-1]
    l1[size-1]=temp
    print(l1)
l1=[]
n=int(input("Enter the size :"))
for i in range(1,n+1):
    data=int(input("Enter the data :"))
    l1.append(data)
print(l1)
listswap(l1)


# GET INDEX FROM USER TO SWAP ON LIST DATA 
def listswap(l1):
    x=int(input("Enter the 1st swap index :"))
    y=int(input("Enter the 2nd swap index :"))
    a=0
    a=l1[x]
    l1[x]=l1[y]
    l1[y]=a
    print(l1)
l=[]
n=int(input("Enter the size :"))
for i in range(1,n+1):
    data=int(input("Enter the data :"))
    l.append(data)
print(l)
listswap(l)    

 
# list2D diagonal sum:
def list2D(l1):
    sum=0
    for x in range(len(l1)):
        for y in range(len(l1[x])):
            if(x+y==2):
               sum=sum+l1[x][y]
               print(l1[x][y],end='')
        print("  =  ",sum)
    print("sum is :",sum)
l1=[[1,2,3],[4,5,6],[7,8,9]] 
list2D(l1)               

# arbitary function program:
def sum(*l1):
    sum=0
    for x in l1:
        sum=sum+x
    print("sum is :",sum)    
sum(10)
sum(10,20,30)
sum(10,20)
sum(10,20,30,40)
sum(10,20,30,40,50)   


# name argument function program:

def sum(x=100,y=200):
    print("sum is :",x+y)
    print(x,y)
sum()
sum(10,20)
sum(x=50,y=60)
sum(y=90,x=10)    
