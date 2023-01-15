#armstrong no
num1=int(input('enter the no'))
num2=num1
sum1=0
while num1>0:
    digit=num1%10
    sum1+=digit**3
    num1//=10
if sum1==num2:
    print('the no',num2,'is an armstrong no')
else:
    print('the no',num2,'is not an armstrong no')
