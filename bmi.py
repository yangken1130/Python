hcm=eval(input())
w=eval(input())
h=hcm/100
bmi=w/(h*h)

print('%.2f'%bmi)
if bmi<18.5:
    print('Underweight')
elif bmi>=18.5 and bmi<24:
    print('Normal')
elif bmi>=24 and bmi<27:
    print('Overweight')
elif bmi>=27 and bmi<30:
    print('Obese Class I')
elif bmi>=30 and bmi<35:
    print('Obese Class II')
elif bmi>=35:
    print('Obese Class III')
