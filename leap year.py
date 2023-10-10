year=int(input("enter the year"))

if(year%100==0 and year%400==0):
    print("Thte year is leap year")

elif(year%100!=0 and year%4==0):
    print("The year is leap year")
        
else:
    print("The year is not a leap year")    