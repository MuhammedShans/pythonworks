# from re import *
# text="abcdABCD$%&7e9fk"
# pattern="[^A-Za-z0-9]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

# # print(count)  



# from re import *
# text="abcdeABioCD$%&7e9fk"
# pattern="[a e i o u A E I O U]"

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())



from re import *
text="abcdeABioCD$%&7e9fk"
pattern="[^aeiouAEIOU\W\d]"

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())


