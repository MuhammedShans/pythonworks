name=input("enter a name: ")
num=int(input("enter a number: "))
if num<10:
    for i in range(1,num+1):
        print(name)
else:
    print("Too high")    