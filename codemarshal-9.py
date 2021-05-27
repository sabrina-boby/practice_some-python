
'1 2 3 4 5'.split()
[1,2,3,4,5]
n=int(input())
t=0

sum=0
for i in range(n):
    numbers = list(map(int, input().split()))
    for j in numbers:
        t += j

    ans = (t-numbers[0])/numbers[0]
    print('Case ',i+1,': ',int(ans))
    
    t = 0