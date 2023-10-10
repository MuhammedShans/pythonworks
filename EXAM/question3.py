lst = [2, 3, 4, 5]
sum=int(input("enter a number:"))
pair=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==sum:
            pair.append((lst[i],lst[j]))
print(pair)