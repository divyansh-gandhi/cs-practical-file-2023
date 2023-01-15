#ques9
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("Greatest Common Divisor (GCD) is ", gcd)
if num1 > num2:
    greater = num1
else:
    greater = num2
while(True):
    if((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 1
print("The Least Common Multiple (LCM) is ", lcm)
