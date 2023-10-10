# from re import *
# text="aabbcaabdaaa"

# pattern="a+"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group(),m.start())




from re import *

phone=input("enter the phone number")


rule="\d{10}"

matcher=fullmatch(rule,phone)

if(matcher==None):
    print("invalid")
else:
    print("valid")    