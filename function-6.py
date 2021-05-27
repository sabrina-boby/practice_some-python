
def evg(a):
    sum=0
    count=0
    for i in a:
        sum=sum+i
        count=count+1
    return sum/count       

a=evg([5,8,9,7,4])
print(a)