#15
list1 = []
number = int(input('How many elements to put in List: '))
for n in range(number):
    element = int(input('Enter element '))
    list1.append(element)
print("Maximum element in the list is :", max(list1))
print("Minimum element in the list is :", min(list1))
