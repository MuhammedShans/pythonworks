text="ABCDA"
wc={}

for ch in text:
    if ch in wc:
        print("The first recursive characteris",ch)
        break

    else:
        wc[ch]=1


            