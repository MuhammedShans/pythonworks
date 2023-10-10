lst=[2,3,5,7,4]
sum=9
lst.sort()

low=0
upper=len(lst)-1

while(low<upper):
    cur_sum=lst[low]+lst[upper]
    if cur_sum==sum:
        print("pairs",lst[low],lst[upper])
        low+=1
    elif cur_sum<sum:
        low+=1
    else:
        upper-=1    