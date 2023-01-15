def factorial(n):
    prod=1
    for i in range(n,0,-1):
        product=prod*(i)
    return prod

x=int(input('enter the value of x'))
n=int(input('enter the value of n'))

sum1=0
for j in range(1,n+1):
    prod=factorial(j)
    if j%2!=0:
        sum1-=(x**j)/(factorial(j))
    else:
        sum1+=(x**j)/(factorial(j))
        
        
print('sum is',sum1)    
    
    

