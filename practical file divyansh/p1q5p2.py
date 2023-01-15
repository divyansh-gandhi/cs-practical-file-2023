x=int(input('enter the value of x'))
n=int(input('enter the value of n'))
sum1=0
for i in range(n+1):
    if i%2!=0:
        sum1+=-x**i
    else:
        sum1+=x**i
print('sum is',sum1)        
    
