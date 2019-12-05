con = "y"
while con=="y" :
    text = input("enter text \n").strip()
    print(text+' kl'+text)
    con = input("Continue?y/n: \n").strip()
    if con == "n":
        break