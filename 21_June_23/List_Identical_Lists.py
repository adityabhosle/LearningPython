dummy1 = []
dummy2 = []

n = int(input("Enter the number of elements \n"))

for i in range(0,n):
    elem = int(input("For the first list, enter element - {} - ".format(i+1)))
    # appending this input to the list
    dummy1.append(elem)

for i in range(0,n):
    elem = int(input("For the second list, enter element - {} - ".format(i+1)))
    # appending this input to the list
    dummy2.append(elem)

# sort both the lists
dummy1.sort()
dummy2.sort()

# check if the lists entered are identical
if dummy1 == dummy2:
    print("Both your lists are identical")
else:
    print("The lists are not identical")