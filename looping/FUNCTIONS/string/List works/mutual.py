all_users=["mohanlal","fahad","unni","mammooty","nivin"]
nivin_frnds=["mohanlal","fahad","unni"]
fahad_frnds=["mohanlal","unni","mammooty"]
mutualfrnds=[]
for f in nivin_frnds:
    if f in fahad_frnds:
        mutualfrnds.append(f)
print(mutualfrnds)    