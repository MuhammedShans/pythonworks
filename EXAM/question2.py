text="pycharm is an ide"
word=text.split(" ")
longest_word=max(word,key=lambda w:len(w)) 
print(longest_word)