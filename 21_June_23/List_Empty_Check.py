dummy = []

n = int(input("Enter the number of elements \n"))

for i in range(0,n):
    elem = int(input("Enter element - {} - ".format(i)))
    #appending this input to the list
    dummy.append(elem)

if not dummy:
    print("Empty list\n")
else:
    print("Not an empty list - ", dummy)

