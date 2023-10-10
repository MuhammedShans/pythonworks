f=open("C:/Users/abhij/Desktop/python_work/looping/FUNCTIONS/string/List works/fileinput/data.txt","r")

words=[line.rstrip("\n") for line in f]
longest_word=max(words,key=lambda w:len(w)) 
print(longest_word)