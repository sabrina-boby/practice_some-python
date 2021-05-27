from random import randint


for i in range(1,6):
    n=int(input("Enter your guess between 1 to 5 : "))
    R=randint(1,5)


    if n==R:
        print("right")
    else:
        print("wrong")  
        print("right was = ",R)