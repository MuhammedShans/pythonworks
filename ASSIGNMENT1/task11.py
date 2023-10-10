numpep=(input("how many people you wants to invinite to the party: "))

def invitepep():
    for i in range(numpep):
        name=input(f"enter the name of peoples {i + 1}: ")
        print(f"{name} has been invited")
    else:
        print("Too many peoples") 

invitepep()           