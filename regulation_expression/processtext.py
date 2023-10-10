from re import *

f=open("C:\\Users\\abhij\\Desktop\\python_work\\regulation_expression\\data.txt")

phone_rules="\d{10}"

mail_rule="[\w]+@gmail.com"
phone_numbers=[]
mail_ids=[]
for line in f:
    words=line.rstrip("\n").split()
    for w in words:
        matcher=fullmatch(phone_rules,w)
        email_matcher=fullmatch(mail_rule,w)
        if matcher!=None:
            phone_numbers.append(w)
        elif email_matcher!=None:
            mail_ids.append(w)    

print(phone_numbers)            