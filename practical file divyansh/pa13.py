#13
list1=eval(input("Enter a list "))
print("Original List is:",list1)
s=len(list1)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    list1[i],list1[i+1]=list1[i+1],list1[i]
print("List after swapping :",list1)
