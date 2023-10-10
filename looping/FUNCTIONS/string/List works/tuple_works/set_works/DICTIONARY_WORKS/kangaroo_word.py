sorce_word="decreased"
target_word="desease"
wc={}

for ch in sorce_word:
    if ch in wc:
        wc[ch]+=1

    else:
        wc[ch]=1

for ch in target_word:
    if ch in wc and wc.get(ch)>0:
        wc[ch]-=1

    else:
        is_kangaroo=False
        break    
print(wc)          