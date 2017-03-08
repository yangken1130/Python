sum=0
n=eval(input())
for i in range(1,n+1):
    sum+=i
    print(i,end='')
    if i!=n:
        print('+',end='')
print(' =',sum)
