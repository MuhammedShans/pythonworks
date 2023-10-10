year=(int(input("enter the year")))

result="leap year" if year%100==0 and year%400==0 else "leap year" if year%100!=0 and year%4==0 else "not leap year"
print(result)