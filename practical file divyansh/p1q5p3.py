x=int(input('enter the value of x'))
n=int(input('enter the value of n'))
sum1=0
for i in range(1,n+1):
    if i%2==0:
        sum1-=(x**i)/i
    else:
        sum1+=(x**i)/i
print('sum is',sum1)

        
