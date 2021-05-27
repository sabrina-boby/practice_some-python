

store=False
while not store:
    n=int(input("Enter a numb : "))
    m=int(input("Enter a numb : "))

    while True:
        operation=input("Enter add/sub : ") 
        
        if operation=="quit":
            store=True
            break
        if operation not in ["add", "sub"]:
            print("enter valid item")
            continue
        if operation=="add":
            print(n," + ",m," = ",n+m)  
            break
        if operation=="sub":
            print(n," - ",m," = ",n-m)  
            break

