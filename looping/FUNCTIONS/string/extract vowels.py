text="sunil gavaskar had a no-holds-barred remark on overseas commentators"

vowels="a","e","i","o","u"
words=text.split(" ")
for w in words:
    if w.casefold().startswith(vowels):
        print(w)