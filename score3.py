year=eval(input())
if year==1:
    score=eval(input())
    if score>=60 and score<=100:
        print('pass')
    elif score<60 and score>0:
        print('fail')
    else:
        print('score error')
elif year==2:
    score=eval(input())
    if score>=70 and score<=100:
        print('pass')
    elif score<70 and score>0:
        print('fail')
    else:
        print('score error')
else:
    print('roll error')
