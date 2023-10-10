tweets="What a game, hats off to both teams.well done @benstoke38 @pacccum1"


words=tweets.split(" ")

for w in words:
    if w.startswith("@"):
        print(w)
    