#14
list1 = []
print("Enter 5 elements for the list: ")
for i in range(0,5):
    value = int(input('enter the value'))
    list1.append(value)
print("Enter an element to be search: ")
element = int(input(' enter the element '))
for i in range(5):
    if element == list1[i]:
        print("Element found at Index:", i)
        print("Element found at Position:", i+1)
