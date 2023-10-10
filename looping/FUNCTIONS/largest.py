a= int(input("enter the first number :"))
b= int(input("enter the second number :"))
c= int(input("enter the third number :"))

def largest(a,b,c):
    if a>b and a>c:
        print(a)
    elif(b>a) and (c>a):
        print(b) 
    else:
        print(c)      
largest(a,b,c)    