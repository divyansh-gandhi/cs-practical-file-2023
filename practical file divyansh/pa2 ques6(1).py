# a program to input a no
#and check if it is a perfect no
num1=int(input('enter the number :'))
sum1=0
for i in range(1,num1):
    if num1%i==0:
        sum1+=i
if sum1==num1:
    print('the number',num1,'is a perfect no')
else:
    print('the number',num1,'is not a perfect no')

    
