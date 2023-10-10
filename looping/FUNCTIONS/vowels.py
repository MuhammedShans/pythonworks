word=input("enter the word :")

def vowelscount(word):
    v_count=0
    c_count=0
    for i in range(len(word)): 
        if word[i] in ['a','e','i','o','u']:
            v_count=v_count+1
        else:
            c_count=c_count+1
    print(v_count)
    print(c_count)
vowelscount(word)        
