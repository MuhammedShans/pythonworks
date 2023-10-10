def add(n1,n2):
    res=n1+n2
    return res
print(add(10,20))




def cube(n):
    res=n**3
    return res
print(cube(3))


def sub(n1,n2):
    res=n1-n2
    return res
print(sub(10,5))


def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
        
print(smart_sub(5,10))