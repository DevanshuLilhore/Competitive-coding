'''
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter a number :"))
x=factorial(n)
print("factorial of ",n," :",x)

def area(n):
    d=n/2
    a=3.14*d*d
    return a
n=int(input("Enter diametar of circle :"))
x=area(n)
print("area of circle :",x)

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

def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if c==2:
        print("prime number :",n,"Square root : ",n/2)
    else:
        print("not prime number :",n)
n=int(input("Enter a number : "))
prime(n)

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

def Great(n1,n2,n3):
    print("Smallest number :",end="")
    if n1<n2 and n1<n3:
        print(n1)
    else:
        if n2<n3:
            print(n2)
        else:
            print(n3)
Great(5,3,5)

def Great(n1,n2,n3):
    print("Smallest number :",end="")
    if n1>=n2 and n1>=n3:
        if(n2>=n3):
            print(n2)
        else:
            print(n3)
    else:
        if n2>=n1 and n2>=n3:
            if(n1>=n3):
                print(n1)
            else:
                print(n3)
        else:
            if(n1>=n2):
                print(n1)
            else:
                print(n2)
Great(5,3,4)
'''
