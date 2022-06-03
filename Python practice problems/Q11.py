def palidrome(str):
    str=str.lower()
    rev=str[::-1]
    if str==rev:
        print ("String is palidrome.")
    else:
        print("Not a palidrome")

palidrome('Malayalam')
palidrome("RoboISM")
