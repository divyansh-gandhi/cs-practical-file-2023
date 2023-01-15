#a pallidrom
num1=int(input('enter the no :'))
num2=num1
reverse=0
while num1>0:
    digit=num1%10
    reverse=reverse*10+digit
    num1//=10
if num2==reverse:
    print('the number is a palindrom')
else:
    print('the number is not a palindrom')
    
    
