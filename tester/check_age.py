age = "66m"

if age[-1].isalpha() and age[:-1].isnumeric():
    print("המבנה תקין")
    op = ["D","W","M","Y"]
    if age[-1].upper() in op:
        print("אות התקופה תקין")
    else:
        print("אות התקופה לא תקין")
else:
    print("המבנה לא תקין")




# or age[-1] != "W" or age[-1] != "M" or age[-1] != "Y":