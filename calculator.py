a=eval(input())
b=eval(input())
s=input()

if s=='+':
    ans=a+b
    print('%.2f'%a,s,'%.2f'%b,'=','%.2f'%ans)
elif s=='-':
    ans=a-b
    print('%.2f'%a,s,'%.2f'%b,'=','%.2f'%ans)

elif s=='*':
    ans=a*b
    print('%.2f'%a,s,'%.2f'%b,'=','%.2f'%ans)
elif s=='/':
    ans=a/b
    print('%.2f'%a,s,'%.2f'%b,'=','%.2f'%ans)
