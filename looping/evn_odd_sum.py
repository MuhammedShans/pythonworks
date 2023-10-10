start=10
end=20
evn_sum=0
odd_sum=0

while(start<=end):
    if start%2==0:
        evn_sum=evn_sum+start
        
    else:
        odd_sum=odd_sum+start
    start+=1  
print("even sum",evn_sum)
print("odd sum",odd_sum)              