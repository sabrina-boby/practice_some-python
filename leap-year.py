

year=int(input("enter any year : "))

if year % 4 != 0:
    print("NO")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")