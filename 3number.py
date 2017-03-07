a=eval(input())
b=eval(input())
c=eval(input())
l=[a,b,c]
ave=(a+b+c)/3
small=l.index(min(l))
large=l.index(max(l))

print('sum is',a+b+c)
print('average is','%.2f'%ave)
print('product is',a*b*c)
print('smallest is',l[small])
print('largest is',l[large])
