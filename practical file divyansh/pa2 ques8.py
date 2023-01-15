'''a=0
b=1
n=int(input('enter'))
for i in range(1,n+1):
    if i==1:
        print(0,end=' ')
    elif i==2:
        print(1,end=' ')
    c=a+b
    a=c
    b+=c
    print(a,b, end=' ')
'''
def fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ')
        num1 = num2
        num2 = series
        series = num1 + num2
num = int(input('Enter how many numbers needed in Fibonacci series- '))
fibonacci(num)
    
