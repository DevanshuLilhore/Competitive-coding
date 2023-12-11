# factorial
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number :"))
x=factorial(n)
print("factorial of ",n," :",x)

# Area of circle
def area(n):
    d=n/2
    a=3.14*d*d
    return a
n=int(input("Enter diametar of circle :"))
x=area(n)
print("area of circle :",x)

# HCF findout
def GCD(n1,n2):
    hcf=1
    k=n1 if n1<n2 else n2
    for i in range(1,k+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
x=GCD(n1,n2)
print("GCD :",x)

# Cheak prime number
import math
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if c==2:
        print("prime number :",n,"Square root : ",math.sqrt(n))
    else:
        print("not prime number :",n)
n=int(input("Enter a number : "))
prime(n)

# Print prime number between interval
def prime(n1,n2):
    for n1 in range(n1,n2+1):
        c=0
        for i in range(1,n1+1):
            if(n1%i==0):
                c=c+1
        if c==2:
            print(n1)
n1=int(input("Enter num1 number : "))
n2=int(input("Enter num2 number : "))
prime(n1,n2)


# Sum of between interval prime number
def prime(n1,n2):
    sum=0
    for n1 in range(n1,n2+1):
        c=0
        for i in range(1,n1+1):
            if(n1%i==0):
                c=c+1
        if c==2:
            sum=sum+n1
            print(n1,end=" ")
    print("sum of prime number : ",sum)
n1=int(input("Enter num1 number : "))
n2=int(input("Enter num2 number : "))
prime(n1,n2)


# Find largest number between three number
def Great(n1,n2,n3):
    print("Greatest number :",end="")
    if n1>n2 and n1>n3:
        print(n1)
    else:
        if n2>n3:
            print(n2)
        else:
            print(n3)
Great(5,3,5)

# Find smallest number between four number
n1=int(input("Enter a value :"))
n2=int(input("Enter b value :"))
n3=int(input("Enter c value :"))
n4=int(input("Enter c value :"))
if n1<n2:
    if n1<n3:
        if n1<n4:
            print("Smallest number :",n1)
        else:
            print("Smallest number :",n4)
    else:
        if n3<n4:
            print("Smallest number :",n3)
        else:
            print("Smallest number :",n4)
else:
    if n2<n3:
        if n2<n4:
            print("Smallest number :",n2)
        else:
            print("Smallest number :",n4)
    else:
        if n3<n4:
            print("Smallest number :",n3)
        else:
            print("Smallest number :",n4)
    
# Perfect square or not
n=int(input("Enter a number cheak perfect square :"))
i=1
while i:
    s=i*i
    if s==n:
        print("Success",i)
        break
    if s>n:
        print("Failure")
        break
    i+=1
    
# Sum of digit
n=int(input("Enter a number cheak perfect square :"))
sum=0
while n:
    sum+=n%10
    n//=10
print("Sum of digit :",sum)

# split number digit
n=int(input("Enter a number cheak perfect square :"))
sum=0
k=1
m=n
while m:
    k=k*10
    m//=10
print(k)
k//=10
while n:
    sum=n//k
    print(sum,end=" ")
    n%=k
    k//=10

# print box 1 & 0 1111
#                 1001
#                 1111
 n1=int(input("Enter  row :"))
n2=int(input("Enter  colume :"))
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if(i!=1 and i!=5 and j!=1 and j!=5):
            print("0",end="")
        else:
            print("1",end="")
    print()

# Next version print box 1 & 0 1111
#                 1001
#                 1111
n=int(input("Enter a row :"))
m=int(input("Enter a colum :"))
for i in range(1,n+1):
    for j in range(1,m+1):
        if(i==1 or j==m or i==n or j==1):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

# input 12334 
# output 1 2 3 4
n=int(input("Enter a number :"))
l=[]
while n:
    l.append(n%10)
    n//=10
print(l[::-1],end=" ")


# input 12334 
# output 1 2 3 4 useing loop
def re(n):
    if(n==0):
        return
    m=n%10
    re(n//10)
    print(m,end=" ")
    
n=int(input("Enter a number :"))
re(n)

# pair find out in list 
# input list = [12,3,4,4,3,5,5,6,22]
# sum =7
# output= 8 pair given sum :7
l=[12,3,4,4,3,5,5,6,22]
s=7
c=0
for i in range(0,len(l)):
    for j in range(1,len(l)):
        a=l[i]+l[j]
        if s==a:
            c+=1
if c>0:
    print(c,"pair given sum :",s)
else:
    print("No")


""" this type pettern
1
2*2
3*3*3
4*4*4*4
4*4*4*4
3*3*3
2*2
1
"""
n=int(input("Enter a number :"))
for i in range(1,n+1):
    for j in range(1,i):
        print(i,"*",end="")
    print(i,end="")
    print()
for k in range(i,0,-1):
    for m in range(1,k):
        print(k,"*",end="")
    print(k,end="")
    print()
