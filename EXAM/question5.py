from re import*
f=open("C:\\Users\\abhij\\Desktop\\python_work\\EXAM\\pans.txt","w")
pan_id=input("enter a variable:")
rule="[A-Z]{3}[PFACTH][A-Z][\d{4}][a-z]"
matcher=fullmatch(rule,pan_id)
print("invalid" if matcher==None else "valid")