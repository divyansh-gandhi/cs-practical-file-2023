#to check if the no is prime or not
num1=int(input('enter the no;'))
for i in range(2,num1):
    if num1%i==0:
        print('the no is a composite no.')
        break
else:
    print('num is prime')
    
    
