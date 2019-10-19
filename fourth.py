con = "y"
while con=="y" :
    text = input("enter text \n").strip()
    print(text[::-1])
    con = input("Continue?y/n: \n").strip()
    if con == "n":
        break