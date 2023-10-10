all_users=["sachin","dhoni","kohli","rohit","sanju","padikkal"]

sanju_followings=["padikkal","sachin"]

# print suggestion for sanju
suggestions=list(set(all_users).difference(set(sanju_followings)))

sanju_position=suggestions.index("sanju")
suggestions.pop(sanju_position)

print(suggestions)

